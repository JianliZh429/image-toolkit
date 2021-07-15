import os
import time
import cv2


def cv2_save(img, fname, out_dir="./output"):
    """save img to output directory

    Args:
        img ([cv2 image array]): [cv2 image]
        fname ([str]): [filename without prefix and extension]
        out_dir (str, optional): [output directory]. Defaults to "./output".
    """
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    filename = os.path.join(out_dir, "{}_{}.jpg".format(fname, int(time.time())))
    cv2.imwrite(filename, img)


def filename(file_path):
    """parse full path file to filename, without prefix, with extension

    Args:
        file_path ([str]): [full path filename]

    Returns:
        [str]: [filename with extension]
    """
    return file_path.split(os.sep)[-1]


def fname(file_path):
    """parse a full path filename to fname, without prefix and extension

    Args:
        file_path ([str]): [full path filename]
    """
    filename_ = filename(file_path)
    idx = filename_.rindex(os.extsep)

    return filename_[0:idx]
