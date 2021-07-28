import click
import cv2

from files import cv2_save, fname


def dodge(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)


def blend(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result


@click.command()
@click.option("--image_file", type=str, help="Image file of the photo you want to process")
@click.option("--out_dir", default="./output", type=str, help="Output directory to save results")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="Whether to show processing images, press ESC to close window",
)
def sketch(image_file: str, out_dir: str, verbose: int = 0):
    im = cv2.imread(image_file)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inverted, (21, 21), 0, 0)
    blended = dodge(gray, blur)
    # image = 1 - blend(blended, gray)
    if verbose:
        while 1:
            cv2.imshow("sketch", blended)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

    fname_ = fname(image_file)
    cv2_save(blended, fname_, out_dir, "png")


if __name__ == "__main__":
    sketch()
