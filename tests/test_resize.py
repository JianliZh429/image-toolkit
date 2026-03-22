"""Tests for the resize module."""

import os

import cv2
import numpy as np
import pytest
from click.testing import CliRunner

from cli.resize import resize


class TestResizeCommand:
    """Tests for the resize CLI command."""

    def test_resize_width_only(self, sample_image_file: str, temp_dir: str) -> None:
        """Test resizing with width only (aspect ratio preserved)."""
        runner = CliRunner()
        result = runner.invoke(
            resize,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--width", "50"],
        )
        assert result.exit_code == 0
        assert "Resized image saved to" in result.output

    def test_resize_height_only(self, sample_image_file: str, temp_dir: str) -> None:
        """Test resizing with height only (aspect ratio preserved)."""
        runner = CliRunner()
        result = runner.invoke(
            resize,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--height", "50"],
        )
        assert result.exit_code == 0
        assert "Resized image saved to" in result.output

    def test_resize_both_dimensions(self, sample_image_file: str, temp_dir: str) -> None:
        """Test resizing with both width and height."""
        runner = CliRunner()
        result = runner.invoke(
            resize,
            [
                "--image_file",
                sample_image_file,
                "--out_dir",
                temp_dir,
                "--width",
                "50",
                "--height",
                "50",
            ],
        )
        assert result.exit_code == 0
        assert "Resized image saved to" in result.output

    def test_resize_no_dimensions(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that resize fails without dimensions."""
        runner = CliRunner()
        result = runner.invoke(resize, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_resize_file_not_found(self, temp_dir: str) -> None:
        """Test that resize fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(
            resize,
            [
                "--image_file",
                "/nonexistent/image.jpg",
                "--out_dir",
                temp_dir,
                "--width",
                "50",
            ],
        )
        assert result.exit_code == 1
        assert "Error" in result.output


class TestResizeOutput:
    """Tests for resize output verification."""

    def test_resize_dimensions_correct(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that output image has correct dimensions."""
        runner = CliRunner()
        runner.invoke(
            resize,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--width", "50"],
        )

        # Find the output file
        output_files = [f for f in os.listdir(temp_dir) if f.endswith(".jpeg")]
        assert len(output_files) == 1

        output_path = os.path.join(temp_dir, output_files[0])
        output_img = cv2.imread(output_path)
        assert output_img is not None
        assert output_img.shape[1] == 50  # Width should be 50
