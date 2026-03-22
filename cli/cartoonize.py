"""Cartoon effect - applies cartoon/cartoon painting effects to images."""

import os

import click
import cv2

from cli.files import cv2_save, fname


@click.command()
@click.option("--image_file", type=str, required=True, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option(
    "--bilateral_filters",
    default=4,
    type=int,
    help="Number of bilateral filter iterations (more = smoother)",
)
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display intermediate results (press ESC to close)",
)
def cartoonize(
    image_file: str,
    out_dir: str,
    bilateral_filters: int,
    verbose: int = 0,
) -> None:
    """Apply cartoon effect to an image.

    Uses bilateral filtering for edge preservation and adaptive thresholding
    to create a cartoon-like appearance. Outputs intermediate steps:
    grayscale, edge sketch, and final painting.
    """
    if not os.path.exists(image_file):
        click.echo(f"Error: Input image not found: {image_file}", err=True)
        raise SystemExit(1)

    fname_ = fname(image_file)

    im = cv2.imread(image_file)
    if im is None:
        click.echo(f"Error: Failed to read image: {image_file}", err=True)
        raise SystemExit(1)

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    # Apply bilateral filters for smoothing while preserving edges
    for _ in range(bilateral_filters):
        im = cv2.bilateralFilter(im, 15, 30, 20)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2_save(gray, fname_, out_dir, suffix="gray")
    click.echo(f"Grayscale saved to: {os.path.join(out_dir, fname_)}_gray.jpg")

    # Create edge mask using adaptive thresholding
    blur = cv2.medianBlur(gray, 7)
    im_edge = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)
    cv2_save(im_edge, fname_, out_dir, suffix="sketch")
    click.echo(f"Edge sketch saved to: {os.path.join(out_dir, fname_)}_sketch.jpg")

    # Combine edges with color image
    rgb = cv2.cvtColor(im_edge, cv2.COLOR_GRAY2RGB)
    image = cv2.bitwise_and(im, rgb)
    cv2_save(image, fname_, out_dir, suffix="painting")
    click.echo(f"Cartoon painting saved to: {os.path.join(out_dir, fname_)}_painting.jpg")


if __name__ == "__main__":
    cartoonize()
