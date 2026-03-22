"""Tests for the sketch module."""

import os

import cv2
import numpy as np
import pytest
from click.testing import CliRunner

from cli.sketch import sketch, dodge, blend


class TestDodgeBlend:
    """Tests for dodge and blend helper functions."""

    def test_dodge_function(self) -> None:
        """Test dodge blending function."""
        image = np.full((10, 10), 128, dtype=np.uint8)
        mask = np.full((10, 10), 100, dtype=np.uint8)
        result = dodge(image, mask)
        assert result.shape == image.shape
        assert result.dtype == np.uint8

    def test_blend_function(self) -> None:
        """Test blend function."""
        front = np.full((10, 10, 3), 100, dtype=np.float32)
        back = np.full((10, 10, 3), 50, dtype=np.float32)
        result = blend(front, back)
        assert result.shape == front.shape


class TestSketchCommand:
    """Tests for the sketch CLI command."""

    def test_sketch_basic(self, sample_image_file: str, temp_dir: str) -> None:
        """Test basic sketch conversion."""
        runner = CliRunner()
        result = runner.invoke(sketch, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 0
        assert "Sketch saved to" in result.output

    def test_sketch_file_not_found(self, temp_dir: str) -> None:
        """Test sketch fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(sketch, ["--image_file", "/nonexistent/image.jpg", "--out_dir", temp_dir])
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_sketch_creates_output(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that sketch creates output file."""
        runner = CliRunner()
        runner.invoke(sketch, ["--image_file", sample_image_file, "--out_dir", temp_dir])

        output_files = [f for f in os.listdir(temp_dir) if f.endswith(".png")]
        assert len(output_files) >= 1


class TestSketchOutput:
    """Tests for sketch output verification."""

    def test_sketch_output_is_grayscale(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that sketch output is grayscale."""
        runner = CliRunner()
        runner.invoke(sketch, ["--image_file", sample_image_file, "--out_dir", temp_dir])

        output_files = [f for f in os.listdir(temp_dir) if f.endswith(".png")]
        assert len(output_files) >= 1

        output_path = os.path.join(temp_dir, output_files[0])
        output_img = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        assert output_img is not None
        assert len(output_img.shape) == 2  # Grayscale has 2 dimensions
