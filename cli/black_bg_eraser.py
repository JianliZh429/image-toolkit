"""Black background eraser - removes black backgrounds from images."""

import os

import click
import cv2
import numpy as np

from cli.files import cv2_save, fname


@click.command()
@click.option("--image_file", type=str, required=True, help="Path to the input image file")
@click.option("--out_dir", default="./output", type=str, help="Output directory for results")
@click.option(
    "--threshold",
    default=10,
    type=int,
    help="Threshold value for binary thresholding (0-255)",
)
@click.option(
    "--margin",
    default=0,
    type=int,
    help="Margin to crop from edges before processing",
)
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="If set, display intermediate results (press ESC to close)",
)
def erase(
    image_file: str,
    out_dir: str,
    threshold: int = 10,
    margin: int = 0,
    verbose: int = 0,
) -> None:
    """Remove black backgrounds from images.

    Uses thresholding and contour detection to identify the main subject
    and replaces the background with white.
    """
    if not os.path.exists(image_file):
        click.echo(f"Error: Input image not found: {image_file}", err=True)
        raise SystemExit(1)

    im = cv2.imread(image_file)
    if im is None:
        click.echo(f"Error: Failed to read image: {image_file}", err=True)
        raise SystemExit(1)

    height, width = im.shape[:2]  # type: ignore[union-attr]

    # Apply margin crop if specified
    if margin > 0:
        im = im[margin : height - margin, margin : width - margin]
        height, width = im.shape[:2]  # type: ignore[union-attr]

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Apply threshold to identify dark areas
    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    if verbose:
        cv2.imshow("thresh", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Find contours and select the largest one
    contours_result = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours_result[0] if len(contours_result) == 2 else contours_result[1]

    if not contours:
        click.echo("Error: No contours found in image", err=True)
        raise SystemExit(1)

    contour = max(contours, key=cv2.contourArea)  # type: ignore[call-overload]

    # Replace background with white
    img = im.copy()  # type: ignore[union-attr]
    for i in range(height):
        for j in range(width):
            if cv2.pointPolygonTest(contour, (j, i), True) <= 0:
                img[i, j] = [255, 255, 255]

    if verbose:
        cv2.imshow("processed", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    fname_ = fname(image_file)
    output_path = cv2_save(img, fname_, out_dir)
    click.echo(f"Processed image saved to: {output_path}")


if __name__ == "__main__":
    erase()
