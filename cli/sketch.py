"""Sketch converter - transforms images into pencil sketch style."""

import os

import click
import cv2
import numpy as np

from cli.files import cv2_save, fname


def dodge(image: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Apply dodge blending mode to image.

    Args:
        image: Source image array.
        mask: Mask array for blending.

    Returns:
        Blended image array.
    """
    return cv2.divide(image, 255 - mask, scale=256)


def blend(front: np.ndarray, back: np.ndarray) -> np.ndarray:
    """Apply blend mode to foreground and background.

    Args:
        front: Foreground image array.
        back: Background image array.

    Returns:
        Blended image array.
    """
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result  # type: ignore[no-any-return]


@click.command()
@click.option("--image_file", type=str, required=True, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display the sketch result (press ESC to close)",
)
def sketch(image_file: str, out_dir: str, verbose: int = 0) -> None:
    """Convert an image to pencil sketch style.

    Uses Gaussian blur and dodge blending to create a sketch effect
    suitable for avatars or artistic presentations.
    """
    if not os.path.exists(image_file):
        click.echo(f"Error: Input image not found: {image_file}", err=True)
        raise SystemExit(1)

    im = cv2.imread(image_file)
    if im is None:
        click.echo(f"Error: Failed to read image: {image_file}", err=True)
        raise SystemExit(1)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inverted, (21, 21), 0, 0)
    blended = dodge(gray, blur)

    if verbose:
        cv2.imshow("sketch", blended)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    fname_ = fname(image_file)
    output_path = cv2_save(blended, fname_, out_dir, suffix="png", ext="png")
    click.echo(f"Sketch saved to: {output_path}")


if __name__ == "__main__":
    sketch()
