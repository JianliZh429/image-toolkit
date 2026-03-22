"""Tests for the main CLI entry point."""

from click.testing import CliRunner

from cli.main import cli


class TestMainCLI:
    """Tests for the main CLI group."""

    def test_cli_help(self) -> None:
        """Test CLI help command."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Image Toolkit" in result.output
        assert "license-photo" in result.output
        assert "resize" in result.output
        assert "sketch" in result.output
        assert "black-bg-eraser" in result.output
        assert "cartoonize" in result.output

    def test_cli_version(self) -> None:
        """Test CLI version command."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "0.1.1" in result.output

    def test_cli_subcommand_help(self) -> None:
        """Test subcommand help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["resize", "--help"])
        assert result.exit_code == 0
        assert "--width" in result.output
        assert "--height" in result.output

    def test_cli_license_photo_help(self) -> None:
        """Test license-photo subcommand help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["license-photo", "--help"])
        assert result.exit_code == 0
        assert "--image_file" in result.output
        assert "--country" in result.output
