"""Image Toolkit - Unified CLI entry point for all image processing tools."""

import click

from cli import __version__
from cli.license_photo import processing as license_photo_cmd
from cli.resize import resize as resize_cmd
from cli.sketch import sketch as sketch_cmd
from cli.black_bg_eraser import erase as black_bg_eraser_cmd
from cli.cartoonize import cartoonize as cartoonize_cmd


@click.group()
@click.version_option(version=__version__, prog_name="image-toolkit")
def cli() -> None:
    """Image Toolkit - A collection of image processing tools using OpenCV.

    Use `image-toolkit COMMAND --help` for more information on a specific command.
    """
    pass


cli.add_command(license_photo_cmd, "license-photo")
cli.add_command(resize_cmd, "resize")
cli.add_command(sketch_cmd, "sketch")
cli.add_command(black_bg_eraser_cmd, "black-bg-eraser")
cli.add_command(cartoonize_cmd, "cartoonize")


if __name__ == "__main__":
    cli()
