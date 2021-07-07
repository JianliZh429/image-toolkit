import os

import click
import cv2
import numpy as np


BACKGROUND_COLORS = [(221, 140, 61), (0, 0, 255), (255, 255, 255)]
BACKGROUND_COLORS_NAMES = ["blue", "red", "white"]
TARGET_SIZES = {1: (295, 413), 2: (413, 579)}


def grab_cut(image_file, out_dir, tz, verbose=1):
    im = cv2.imread(image_file)
    height, width = im.shape[:2]
    mask = np.zeros(im.shape[:2], np.uint8)
    bgd = np.zeros((1, 65), np.float64)
    fgd = np.zeros((1, 65), np.float64)
    rect = (0, 0, width - 1, height - 1)

    cv2.grabCut(im, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    img = im * mask2[:, :, np.newaxis]

    for name, tz_color in zip(BACKGROUND_COLORS_NAMES, BACKGROUND_COLORS):
        _img = img.copy()
        _img[np.where((_img == (0, 0, 0)).all(axis=2))] = tz_color
        _img = cv2.resize(_img, TARGET_SIZES[tz], interpolation=cv2.INTER_AREA)

        cv2.imwrite(os.path.join(out_dir, "{}_{}.jpg".format(tz, name)), _img)

    if verbose:
        while 1:
            cv2.imshow("im", img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

    cv2.destroyAllWindows()


@click.command()
@click.option("--image_file", type=str, help="Image file of the photo you want to process")
@click.option("--out_dir", default="./output", type=str, help="Output directory to save results")
@click.option(
    "--tz",
    default=1,
    type=int,
    help="Output image size: 1 is for 1 inch, 2 is for 2 inches",
)
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="Whether to show processing images, press ESC to close window",
)
def processing(image_file, out_dir, tz, verbose):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    grab_cut(image_file, out_dir, tz, verbose=verbose)


if __name__ == "__main__":
    processing()
