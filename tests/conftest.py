"""Test configuration and fixtures for image-toolkit tests."""

import os
import tempfile
from typing import Generator

import cv2
import numpy as np
import pytest


@pytest.fixture
def temp_dir() -> Generator[str, None, None]:
    """Create a temporary directory for test outputs.

    Yields:
        Path to temporary directory.
    """
    temp = tempfile.mkdtemp()
    yield temp
    # Cleanup is handled by tempfile


@pytest.fixture
def sample_image() -> np.ndarray:
    """Create a sample test image.

    Returns:
        A 100x100 RGB image with a simple pattern.
    """
    # Create a simple gradient image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    for i in range(100):
        for j in range(100):
            img[i, j] = [i * 2 % 256, j * 2 % 256, (i + j) % 256]
    return img


@pytest.fixture
def sample_image_file(sample_image: np.ndarray, temp_dir: str) -> str:
    """Create a sample image file.

    Args:
        sample_image: Sample image array.
        temp_dir: Temporary directory path.

    Returns:
        Path to the created image file.
    """
    file_path = os.path.join(temp_dir, "test_image.png")
    cv2.imwrite(file_path, sample_image)
    return file_path


@pytest.fixture
def solid_color_image() -> np.ndarray:
    """Create a solid color test image.

    Returns:
        A 50x50 solid blue image.
    """
    return np.full((50, 50, 3), (255, 0, 0), dtype=np.uint8)


@pytest.fixture
def grayscale_image() -> np.ndarray:
    """Create a grayscale test image.

    Returns:
        A 50x50 grayscale gradient image.
    """
    img = np.zeros((50, 50), dtype=np.uint8)
    for i in range(50):
        img[i, :] = i * 5
    return img
