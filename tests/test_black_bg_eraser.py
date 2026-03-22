"""Tests for the black_bg_eraser module."""

import os

import cv2
import numpy as np
import pytest
from click.testing import CliRunner

from cli.black_bg_eraser import erase


class TestEraseCommand:
    """Tests for the erase CLI command."""

    def test_erase_basic(self, sample_image_file: str, temp_dir: str) -> None:
        """Test basic background erasure."""
        runner = CliRunner()
        result = runner.invoke(erase, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 0
        assert "Processed image saved to" in result.output

    def test_erase_with_threshold(self, sample_image_file: str, temp_dir: str) -> None:
        """Test erasure with custom threshold."""
        runner = CliRunner()
        result = runner.invoke(
            erase,
            [
                "--image_file",
                sample_image_file,
                "--out_dir",
                temp_dir,
                "--threshold",
                "20",
            ],
        )
        assert result.exit_code == 0

    def test_erase_with_margin(self, sample_image_file: str, temp_dir: str) -> None:
        """Test erasure with margin crop."""
        runner = CliRunner()
        result = runner.invoke(
            erase,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--margin", "5"],
        )
        assert result.exit_code == 0

    def test_erase_file_not_found(self, temp_dir: str) -> None:
        """Test erase fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(erase, ["--image_file", "/nonexistent/image.jpg", "--out_dir", temp_dir])
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_erase_creates_output(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that erase creates output file."""
        runner = CliRunner()
        runner.invoke(erase, ["--image_file", sample_image_file, "--out_dir", temp_dir])

        output_files = [f for f in os.listdir(temp_dir) if f.endswith(".jpeg")]
        assert len(output_files) >= 1
