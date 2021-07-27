import click
import cv2
from files import fname, cv2_save


@click.command()
@click.option("--image_file", type=str, help="Image file of the photo you want to process")
@click.option("--out_dir", default="./output", type=str, help="Output directory to save results")
@click.option("--width", default=None, type=int, help="Width, you want your image to be")
@click.option("--height", default=None, type=int, help="Height, you want your image to be")
@click.option(
    "--verbose",
    default=0,
    type=int,
    help="Whether to show processing images, press ESC to close window",
)
def resize(image_file: str, out_dir: str, width: int, height: int, verbose: bool):
    im = cv2.imread(image_file)
    h, w = im.shape[:2]
    shrinking = width < w if width else None or height < h if height else None
    interpolation = cv2.INTER_AREA if shrinking else cv2.INTER_CUBIC

    if width and height:
        image = cv2.resize(im, (width, height), interpolation=interpolation)
    elif width:
        image = cv2.resize(im, (width, int(width / w * h)), interpolation)
    else:
        image = cv2.resize(im, (int(height / h * w), height), interpolation)

    if verbose:
        while 1:
            cv2.imshow("resized", image)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

    fname_ = fname(image_file)
    cv2_save(image, fname_, out_dir)


if __name__ == "__main__":
    resize()
