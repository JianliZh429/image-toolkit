"""Tests for the files utility module."""

import os
import shutil
import tempfile

import cv2
import numpy as np
import pytest

from cli.files import cv2_save, filename, fname


class TestFilename:
    """Tests for filename parsing functions."""

    def test_filename_with_path(self) -> None:
        """Test filename extraction from full path."""
        assert filename("/path/to/image.jpg") == "image.jpg"

    def test_filename_simple(self) -> None:
        """Test filename extraction from simple filename."""
        assert filename("image.jpg") == "image.jpg"

    def test_filename_with_dots(self) -> None:
        """Test filename with multiple dots."""
        assert filename("my.photo.image.jpg") == "my.photo.image.jpg"


class TestFname:
    """Tests for fname (filename without extension) function."""

    def test_fname_with_path(self) -> None:
        """Test fname extraction from full path."""
        assert fname("/path/to/image.jpg") == "image"
        assert fname("/path/to/file.png") == "file"

    def test_fname_simple(self) -> None:
        """Test fname from simple filename."""
        assert fname("image.jpg") == "image"

    def test_fname_with_dots(self) -> None:
        """Test fname with multiple dots in name."""
        assert fname("my.photo.image.jpg") == "my.photo.image"

    def test_fname_no_extension(self) -> None:
        """Test fname when no extension present."""
        assert fname("image") == "image"


class TestCv2Save:
    """Tests for cv2_save function."""

    def test_cv2_save_creates_file(self, sample_image: np.ndarray, temp_dir: str) -> None:
        """Test that cv2_save creates an image file."""
        result_path = cv2_save(sample_image, "test", out_dir=temp_dir, suffix="img")
        assert os.path.exists(result_path)
        assert result_path.endswith(".jpeg")

    def test_cv2_save_creates_directory(self, sample_image: np.ndarray) -> None:
        """Test that cv2_save creates output directory if needed."""
        nested_dir = os.path.join(tempfile.gettempdir(), "test_nested", "dir")
        try:
            result_path = cv2_save(sample_image, "test", out_dir=nested_dir, suffix="img")
            assert os.path.exists(result_path)
        finally:
            # Cleanup
            if os.path.exists(nested_dir):
                shutil.rmtree(nested_dir, ignore_errors=True)

    def test_cv2_save_custom_extension(self, sample_image: np.ndarray, temp_dir: str) -> None:
        """Test cv2_save with custom extension."""
        result_path = cv2_save(sample_image, "test", out_dir=temp_dir, ext="png")
        assert result_path.endswith(".png")

    def test_cv2_save_returns_path(self, sample_image: np.ndarray, temp_dir: str) -> None:
        """Test that cv2_save returns the full path."""
        result_path = cv2_save(sample_image, "test", out_dir=temp_dir, suffix="img")
        expected = os.path.join(temp_dir, "test_img.jpeg")
        assert result_path == expected
