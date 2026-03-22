"""License photo generator - creates ID photos with various background colors.

Supports international passport/ID photo sizes for different countries.
"""

import os
from typing import List, Tuple

import click
import cv2
import numpy as np

from cli.photo_sizes import (
    get_common_size,
    get_inch_size,
    get_size,
    list_countries,
    list_document_types,
)

BACKGROUND_COLORS: List[Tuple[int, int, int]] = [(221, 140, 61), (0, 0, 255), (255, 255, 255)]
BACKGROUND_COLORS_NAMES: List[str] = ["blue", "red", "white"]


def grab_cut(
    image_file: str,
    out_dir: str,
    size: Tuple[int, int],
    verbose: int = 0,
) -> List[str]:
    """Extract foreground from image and generate license photos with different backgrounds.

    Uses GrabCut algorithm to segment the foreground from the background,
    then composites it onto different colored backgrounds for ID photos.

    Args:
        image_file: Path to the input image file.
        out_dir: Directory to save the output images.
        size: Target size as (width, height) in pixels.
        verbose: If non-zero, display intermediate results. Defaults to 0.

    Returns:
        List of paths to saved output images.

    Raises:
        FileNotFoundError: If the input image file does not exist.
        cv2.error: If image processing fails.
    """
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"Input image not found: {image_file}")

    im = cv2.imread(image_file)
    if im is None:
        raise cv2.error(f"Failed to read image: {image_file}")

    height, width = im.shape[:2]
    mask = np.zeros(im.shape[:2], np.uint8)
    bgd: np.ndarray = np.zeros((1, 65), np.float64)
    fgd: np.ndarray = np.zeros((1, 65), np.float64)
    rect = (0, 0, width - 1, height - 1)

    cv2.grabCut(im, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    img = im * mask2[:, :, np.newaxis]

    output_files = []
    for name, tz_color in zip(BACKGROUND_COLORS_NAMES, BACKGROUND_COLORS):
        _img = img.copy()
        _img[np.where((_img == (0, 0, 0)).all(axis=2))] = tz_color
        _img = cv2.resize(_img, size, interpolation=cv2.INTER_AREA)

        output_path = os.path.join(out_dir, f"{name}.jpg")
        cv2.imwrite(output_path, _img)
        output_files.append(output_path)

    if verbose:
        cv2.imshow("im", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return output_files


def print_countries(ctx: click.Context, param: click.Parameter, value: bool) -> None:
    """Callback to print countries and exit."""
    if not value or ctx.resilient_parsing:
        return
    countries = list_countries()
    click.echo("Available country codes:")
    for c in countries:
        click.echo(f"  {c}")
    ctx.exit()


def print_doc_types(ctx: click.Context, param: click.Parameter, value: str) -> None:
    """Callback to print document types and exit."""
    if not value or ctx.resilient_parsing:
        return
    try:
        types = list_document_types(value)
        click.echo(f"Document types for '{value}':")
        for t in types:
            click.echo(f"  {t}")
    except KeyError as e:
        click.echo(f"Error: {e}", err=True)
    ctx.exit()


@click.command()
@click.option("--image_file", type=str, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option(
    "--country",
    "-c",
    default="iso",
    type=str,
    help="Country code for photo size (e.g., 'usa', 'uk', 'jp', 'cn'). "
    "Use 'iso' for ISO standard (35x45mm). Default: iso",
)
@click.option(
    "--doc-type",
    "-d",
    default="iso_216",
    type=str,
    help="Document type: 'passport', 'visa', 'id_card', 'iso_216'. Default: iso_216",
)
@click.option(
    "--size",
    "-s",
    default=None,
    type=str,
    help="Common size alias: 'iso', 'us', 'eu', 'uk', 'jp', 'cn'. " "Overrides --country and --doc-type if specified.",
)
@click.option(
    "--inch",
    "-i",
    default=None,
    type=int,
    help="Legacy inch-based size (1 or 2). Overrides other size options if specified.",
)
@click.option(
    "--width",
    default=None,
    type=int,
    help="Custom width in pixels. Use with --height for custom sizes.",
)
@click.option(
    "--height",
    default=None,
    type=int,
    help="Custom height in pixels. Use with --width for custom sizes.",
)
@click.option(
    "--list-countries",
    is_flag=True,
    expose_value=False,
    is_eager=True,
    callback=print_countries,
    help="List all available country codes and exit.",
)
@click.option(
    "--list-types",
    type=str,
    expose_value=False,
    is_eager=True,
    callback=print_doc_types,
    help="List document types for a specific country code.",
)
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display intermediate results (press ESC to close).",
)
def processing(
    image_file: str,
    out_dir: str,
    country: str,
    doc_type: str,
    size: str,
    inch: int,
    width: int,
    height: int,
    verbose: int,
) -> None:
    """Generate license photos with different background colors.

    This tool extracts the person from an image and creates ID-style photos
    with blue, red, and white backgrounds in standard sizes.

    \b
    Examples:
        # ISO standard (35x45mm)
        image-toolkit license-photo --image_file photo.jpg

        # US passport (2x2 inches)
        image-toolkit license-photo --image_file photo.jpg --country usa

        # UK visa
        image-toolkit license-photo --image_file photo.jpg -c uk -d visa

        # Using common size alias
        image-toolkit license-photo --image_file photo.jpg -s us

        # Custom size
        image-toolkit license-photo --image_file photo.jpg --width 600 --height 600
    """
    # Require image_file for processing
    if not image_file:
        click.echo("Error: --image_file is required", err=True)
        raise SystemExit(1)

    # Determine target size
    target_size: Tuple[int, int]

    if inch is not None:
        # Legacy inch-based size
        try:
            target_size = get_inch_size(inch)
            size_info = f"{inch} inch (legacy)"
        except KeyError as e:
            click.echo(f"Error: {e}", err=True)
            raise SystemExit(1)

    elif size is not None:
        # Common size alias
        try:
            target_size = get_common_size(size)
            size_info = f"'{size}' common size"
        except KeyError as e:
            click.echo(f"Error: {e}", err=True)
            raise SystemExit(1)

    elif width is not None and height is not None:
        # Custom size
        target_size = (width, height)
        size_info = f"custom ({width}x{height})"

    elif width is not None or height is not None:
        click.echo("Error: Both --width and --height must be specified for custom size", err=True)
        raise SystemExit(1)

    else:
        # Country and document type
        try:
            target_size = get_size(country, doc_type)
            size_info = f"{country}/{doc_type}"
        except KeyError as e:
            click.echo(f"Error: {e}", err=True)
            raise SystemExit(1)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    try:
        output_files = grab_cut(image_file, out_dir, target_size, verbose=verbose)
        click.echo(f"Generated {len(output_files)} license photos ({size_info}) in {out_dir}")
        for f in output_files:
            click.echo(f"  - {f}")
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)
    except cv2.error as e:
        click.echo(f"Image processing error: {e}", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    processing()
