"""Utility functions for file operations and image saving."""

import os
import time

import cv2
import numpy as np


def cv2_save(
    img: np.ndarray,
    fname: str,
    out_dir: str = "./output",
    suffix: str = "",
    ext: str = "jpeg",
) -> str:
    """Save image array to output directory.

    Args:
        img: OpenCV image array (numpy ndarray).
        fname: Filename without extension.
        out_dir: Output directory path. Defaults to "./output".
        suffix: Suffix to append to filename. If empty, uses timestamp.
        ext: Image file extension (e.g., "jpeg", "png"). Defaults to "jpeg".

    Returns:
        Full path to the saved image file.

    Raises:
        OSError: If the output directory cannot be created.
        cv2.error: If the image cannot be written.
    """
    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    if not suffix:
        suffix = str(int(time.time()))

    filename = os.path.join(out_dir, f"{fname}_{suffix}.{ext}")
    cv2.imwrite(filename, img)

    return filename


def filename(file_path: str) -> str:
    """Parse full path to filename with extension.

    Args:
        file_path: Full path to the file.

    Returns:
        Filename with extension (e.g., "image.jpg").
    """
    return os.path.basename(file_path)


def fname(file_path: str) -> str:
    """Parse full path to filename without extension.

    Args:
        file_path: Full path to the file.

    Returns:
        Filename without extension (e.g., "image" from "/path/to/image.jpg").
    """
    filename_ = filename(file_path)
    name, _ = os.path.splitext(filename_)
    return name
