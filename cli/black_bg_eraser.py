import click
import cv2
import numpy as np
from files import fname, cv2_save


@click.command()
@click.option("--image_file", type=str, help="Image file of the photo you want to process")
@click.option("--out_dir", default="./output", type=str, help="Output directory to save results")
@click.option("--threshold", default=10, type=int, help="The threshold to cv2.threshold")
@click.option("--margin", default=0, type=int, help="The margin to the interested area")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="Whether to show processing images, press ESC to close window",
)
def erase(image_file, out_dir, threshold=10, margin=0, verbose=0):
    im = cv2.imread(image_file)
    height, width = im.shape[:2]
    im = im[margin : height - margin, margin : width - margin] if margin > 0 else im
    height, width = im.shape[:2]
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    if verbose:
        while 1:
            cv2.imshow("thresh", thresh)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    cv2.destroyAllWindows()

    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    contour = max(contours, key=cv2.contourArea)
    img = im.copy()
    # cv2.drawContours(img, [contour], -1, (0, 0, 255), 3)
    for i in range(height):
        for j in range(width):
            if cv2.pointPolygonTest(contour, (j, i), True) <= 0:
                img[i, j] = [255, 255, 255]

    if verbose:
        while 1:
            cv2.imshow("processed", img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    cv2.destroyAllWindows()

    fname_ = fname(image_file)
    cv2_save(img, fname_, out_dir)


if __name__ == "__main__":
    erase()
