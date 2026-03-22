"""Tests for the license_photo module."""

import os

import cv2
import pytest
from click.testing import CliRunner

from cli.license_photo import grab_cut, processing
from cli.photo_sizes import get_inch_size, get_size


class TestGrabCut:
    """Tests for grab_cut function."""

    def test_grab_cut_creates_outputs(self, sample_image_file: str, temp_dir: str) -> None:
        """Test that grab_cut creates output files."""
        size = get_inch_size(1)
        output_files = grab_cut(sample_image_file, temp_dir, size)
        assert len(output_files) == 3  # blue, red, white backgrounds

    def test_grab_cut_output_names(self, sample_image_file: str, temp_dir: str) -> None:
        """Test output file naming convention."""
        size = get_inch_size(1)
        output_files = grab_cut(sample_image_file, temp_dir, size)
        filenames = [os.path.basename(f) for f in output_files]
        assert any("blue" in f for f in filenames)
        assert any("red" in f for f in filenames)
        assert any("white" in f for f in filenames)

    def test_grab_cut_size_1_inch(self, sample_image_file: str, temp_dir: str) -> None:
        """Test grab_cut with 1 inch size."""
        size = get_inch_size(1)
        output_files = grab_cut(sample_image_file, temp_dir, size)
        for f in output_files:
            img = cv2.imread(f)
            assert img is not None
            assert img.shape[0] == size[1]  # height
            assert img.shape[1] == size[0]  # width

    def test_grab_cut_size_usa_passport(self, sample_image_file: str, temp_dir: str) -> None:
        """Test grab_cut with USA passport size."""
        size = get_size("usa", "passport")
        output_files = grab_cut(sample_image_file, temp_dir, size)
        for f in output_files:
            img = cv2.imread(f)
            assert img is not None
            # USA passport: 600x600
            assert img.shape[0] == 600
            assert img.shape[1] == 600

    def test_grab_cut_file_not_found(self, temp_dir: str) -> None:
        """Test grab_cut with non-existent file."""
        size = get_inch_size(1)
        with pytest.raises(FileNotFoundError):
            grab_cut("/nonexistent/image.jpg", temp_dir, size)


class TestProcessingCommand:
    """Tests for the processing CLI command."""

    def test_processing_basic(self, sample_image_file: str, temp_dir: str) -> None:
        """Test basic license photo processing (ISO default)."""
        runner = CliRunner()
        result = runner.invoke(processing, ["--image_file", sample_image_file, "--out_dir", temp_dir])
        assert result.exit_code == 0
        assert "Generated" in result.output
        assert "iso" in result.output.lower()

    def test_processing_usa_passport(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with USA passport size."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--country", "usa", "--doc-type", "passport"],
        )
        assert result.exit_code == 0
        assert "usa" in result.output.lower()

    def test_processing_common_size_us(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with common US size alias."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--size", "us"],
        )
        assert result.exit_code == 0
        assert "'us'" in result.output

    def test_processing_inch_size(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with legacy inch size."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--inch", "1"],
        )
        assert result.exit_code == 0
        assert "inch" in result.output.lower()

    def test_processing_custom_size(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with custom size."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--width", "500", "--height", "600"],
        )
        assert result.exit_code == 0
        assert "custom" in result.output.lower()

    def test_processing_file_not_found(self, temp_dir: str) -> None:
        """Test processing fails with non-existent file."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", "/nonexistent/image.jpg", "--out_dir", temp_dir],
        )
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_processing_list_countries(self, temp_dir: str) -> None:
        """Test listing available countries."""
        runner = CliRunner()
        result = runner.invoke(processing, ["--list-countries"])
        assert result.exit_code == 0
        assert "Available country codes" in result.output
        assert "usa" in result.output
        assert "uk" in result.output

    def test_processing_list_types(self, temp_dir: str) -> None:
        """Test listing document types for a country."""
        runner = CliRunner()
        result = runner.invoke(processing, ["--list-types", "usa"])
        assert result.exit_code == 0
        assert "Document types for 'usa'" in result.output
        assert "passport" in result.output.lower()

    def test_processing_invalid_country(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with invalid country."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--country", "invalid"],
        )
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_processing_invalid_common_size(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing with invalid common size alias."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--size", "invalid"],
        )
        assert result.exit_code == 1
        assert "Error" in result.output

    def test_processing_partial_custom_size(self, sample_image_file: str, temp_dir: str) -> None:
        """Test processing fails with only width or height specified."""
        runner = CliRunner()
        result = runner.invoke(
            processing,
            ["--image_file", sample_image_file, "--out_dir", temp_dir, "--width", "500"],
        )
        assert result.exit_code == 1
        assert "Error" in result.output
