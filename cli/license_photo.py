"""License photo generator - creates ID photos with various background colors."""

import os
from typing import List, Tuple

import click
import cv2
import numpy as np

BACKGROUND_COLORS: List[Tuple[int, int, int]] = [(221, 140, 61), (0, 0, 255), (255, 255, 255)]
BACKGROUND_COLORS_NAMES: List[str] = ["blue", "red", "white"]
TARGET_SIZES: dict = {1: (295, 413), 2: (413, 579)}


def grab_cut(
    image_file: str,
    out_dir: str,
    tz: int = 1,
    verbose: int = 0,
) -> List[str]:
    """Extract foreground from image and generate license photos with different backgrounds.

    Uses GrabCut algorithm to segment the foreground from the background,
    then composites it onto different colored backgrounds for ID photos.

    Args:
        image_file: Path to the input image file.
        out_dir: Directory to save the output images.
        tz: Target size (1 for 1 inch, 2 for 2 inches). Defaults to 1.
        verbose: If non-zero, display intermediate results. Defaults to 0.

    Returns:
        List of paths to saved output images.

    Raises:
        FileNotFoundError: If the input image file does not exist.
        cv2.error: If image processing fails.
        KeyError: If tz is not a valid size option.
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
        _img = cv2.resize(_img, TARGET_SIZES[tz], interpolation=cv2.INTER_AREA)

        output_path = os.path.join(out_dir, f"{tz}_{name}.jpg")
        cv2.imwrite(output_path, _img)
        output_files.append(output_path)

    if verbose:
        cv2.imshow("im", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return output_files


@click.command()
@click.option("--image_file", type=str, required=True, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option(
    "--tz",
    default=1,
    type=click.IntRange(1, 2),
    help="Output image size: 1 for 1 inch (295x413), 2 for 2 inches (413x579)",
)
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display intermediate results (press ESC to close)",
)
def processing(image_file: str, out_dir: str, tz: int, verbose: int) -> None:
    """Generate license photos with different background colors.

    This tool extracts the person from an image and creates ID-style photos
    with blue, red, and white backgrounds in standard sizes.
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    try:
        output_files = grab_cut(image_file, out_dir, tz, verbose=verbose)
        click.echo(f"Generated {len(output_files)} license photos in {out_dir}")
        for f in output_files:
            click.echo(f"  - {f}")
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)
    except cv2.error as e:
        click.echo(f"Image processing error: {e}", err=True)
        raise SystemExit(1)
    except KeyError:
        click.echo(f"Error: Invalid size option '{tz}'. Use 1 or 2.", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    processing()
