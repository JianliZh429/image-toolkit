"""Image resizing tool - resize images with optional aspect ratio preservation."""

import os
from typing import Optional

import click
import cv2

from cli.files import cv2_save, fname


@click.command()
@click.option("--image_file", type=str, required=True, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option("--width", default=None, type=int, help="Target width in pixels")
@click.option("--height", default=None, type=int, help="Target height in pixels")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display the resized image (press ESC to close)",
)
def resize(
    image_file: str,
    out_dir: str,
    width: Optional[int],
    height: Optional[int],
    verbose: int,
) -> None:
    """Resize an image to specified dimensions.

    If only width or height is provided, the aspect ratio is preserved.
    If both are provided, the image is resized to exact dimensions.
    """
    if not os.path.exists(image_file):
        click.echo(f"Error: Input image not found: {image_file}", err=True)
        raise SystemExit(1)

    if width is None and height is None:
        click.echo("Error: At least one of --width or --height must be specified", err=True)
        raise SystemExit(1)

    im = cv2.imread(image_file)
    if im is None:
        click.echo(f"Error: Failed to read image: {image_file}", err=True)
        raise SystemExit(1)

    h, w = im.shape[:2]

    # Determine interpolation method based on scaling direction
    shrinking = False
    if width is not None and width < w:
        shrinking = True
    elif height is not None and height < h:
        shrinking = True
    interpolation = cv2.INTER_AREA if shrinking else cv2.INTER_CUBIC

    # Calculate new dimensions
    new_w: int
    new_h: int
    if width is not None and height is not None:
        new_w, new_h = width, height
    elif width is not None:
        new_w = width
        new_h = int(width / w * h)
    else:
        assert height is not None
        new_h = height
        new_w = int(height / h * w)

    image = cv2.resize(im, (new_w, new_h), interpolation=interpolation)

    if verbose:
        cv2.imshow("resized", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    fname_ = fname(image_file)
    output_path = cv2_save(image, fname_, out_dir)
    click.echo(f"Resized image saved to: {output_path}")


if __name__ == "__main__":
    resize()
