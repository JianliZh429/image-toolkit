from time import time
import click
import cv2

from files import cv2_save, fname


@click.command()
@click.option("--image_file", type=str, help="Image file of the photo you want to process")
@click.option("--out_dir", default="./output", type=str, help="Output directory to save results")
@click.option("--bilateral_filters", default=4, type=int, help="Number of bilateral filters")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="Whether to show processing images, press ESC to close window",
)
def cartoonize(image_file: str, out_dir: str, bilateral_filters: int, verbose: int = 0):
    fname_ = fname(image_file)

    im = cv2.imread(image_file)
    for i in range(bilateral_filters):
        im = cv2.bilateralFilter(im, 15, 30, 20)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2_save(gray, fname_, out_dir, suffix="gray")

    blur = cv2.medianBlur(gray, 7)
    im_edge = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)
    cv2_save(im_edge, fname_, out_dir, suffix="sketch")

    rgb = cv2.cvtColor(im_edge, cv2.COLOR_GRAY2RGB)
    image = cv2.bitwise_and(im, rgb)
    cv2_save(image, fname_, out_dir, suffix="painting")


if __name__ == "__main__":
    cartoonize()
