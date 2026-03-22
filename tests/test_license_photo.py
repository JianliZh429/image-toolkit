"""Tests for the license_photo module."""

import os

import cv2
import numpy as np
import pytest
from click.testing import CliRunner

from cli.license_photo import processing, grab_cut


class TestGrabCut:
    """Tests for grab_cut function."""

    def test_grab_cut_creates_outputs(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that grab_cut creates output files."""
        output_files = grab_cut(sample_image_file, temp_dir, tz=1)
        assert len(output_files) == 3  # blue, red, white backgrounds

    def test_grab_cut_output_names(self, sample_image_file: str, temp_dir: str) -> None:
        """Test output file naming convention."""
        output_files = grab_cut(sample_image_file, temp_dir, tz=1)
        filenames = [os.path.basename(f) for f in output_files]
        assert any("blue" in f for f in filenames)
        assert any("red" in f for f in filenames)
        assert any("white" in f for f in filenames)

    def test_grab_cut_size_1(self, sample_image_file: str, temp_dir: str) -> None:
        """Test grab_cut with size 1 (1 inch)."""
        output_files = grab_cut(sample_image_file, temp_dir, tz=1)
        for f in output_files:
            img = cv2.imread(f)
            assert img is not None
            # Size 1: 295x413
            assert img.shape[0] == 413
            assert img.shape[1] == 295

    def test_grab_cut_size_2(self, sample_image_file: str, temp_dir: str) -> None:
        """Test grab_cut with size 2 (2 inches)."""
        output_files = grab_cut(sample_image_file, temp_dir, tz=2)
        for f in output_files:
            img = cv2.imread(f)
            assert img is not None
            # Size 2: 413x579
            assert img.shape[0] == 579
            assert img.shape[1] == 413

    def test_grab_cut_file_not_found(self, temp_dir: str) -> None:
        """Test grab_cut with non-existent file."""
        with pytest.raises(FileNotFoundError):
            grab_cut("/nonexistent/image.jpg", temp_dir)


class TestProcessingCommand:
    """Tests for the processing CLI command."""

    def test_processing_basic(self, sample_image_file: str, temp_dir: str) -> None:
        """Test basic license photo processing."""
        runner = CliRunner()
        result = runner.invoke(processing, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 0
        assert "Generated" in result.output

    def test_processing_file_not_found(self, temp_dir: str) -> None:
        """Test processing fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", "/nonexistent/image.jpg", "--out_dir", temp_dir],
        )
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_processing_invalid_size(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with invalid size option."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--tz", "5"],
        )
        assert result.exit_code != 0
