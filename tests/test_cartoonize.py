"""Tests for the cartoonize module."""

import os

import cv2
import numpy as np
import pytest
from click.testing import CliRunner

from cli.cartoonize import cartoonize


class TestCartoonizeCommand:
    """Tests for the cartoonize CLI command."""

    def test_cartoonize_basic(self, sample_image_file: str, temp_dir: str) -> None:
        """Test basic cartoonize effect."""
        runner = CliRunner()
        result = runner.invoke(cartoonize, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 0
        assert "Cartoon painting saved to" in result.output

    def test_cartoonize_with_filters(self, sample_image_file: str, temp_dir: str) -> None:
        """Test cartoonize with custom bilateral filter count."""
        runner = CliRunner()
        result = runner.invoke(
            cartoonize,
            [
                "--image_file",
                sample_image_file,
                "--out_dir",
                temp_dir,
                "--bilateral_filters",
                "2",
            ],
        )
        assert result.exit_code == 0

    def test_cartoonize_file_not_found(self, temp_dir: str) -> None:
        """Test cartoonize fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(
            cartoonize,
            ["--image_file", "/nonexistent/image.jpg", "--out_dir", temp_dir],
        )
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_cartoonize_creates_outputs(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that cartoonize creates multiple output files."""
        runner = CliRunner()
        runner.invoke(cartoonize, ["--image_file", sample_image_file, "--out_dir", temp_dir])

        output_files = os.listdir(temp_dir)
        # Should create gray, sketch, and painting versions
        assert any("gray" in f for f in output_files)
        assert any("sketch" in f for f in output_files)
        assert any("painting" in f for f in output_files)


class TestCartoonizeOutput:
    """Tests for cartoonize output verification."""

    def test_cartoonize_output_exists(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that cartoonize painting output exists."""
        runner = CliRunner()
        runner.invoke(cartoonize, ["--image_file", sample_image_file, "--out_dir", temp_dir])

        output_files = [f for f in os.listdir(temp_dir) if "painting" in f]
        assert len(output_files) >= 1

        output_path = os.path.join(temp_dir, output_files[0])
        assert os.path.exists(output_path)
