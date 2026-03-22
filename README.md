# Image Toolkit

[![CI](https://github.com/JianliZh429/image-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/JianliZh429/image-toolkit/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of image processing tools implemented using OpenCV. Process images from the command line with ease.

## Features

- **License Photo Generator**: Create ID photos with blue, red, or white backgrounds
- **Image Resizer**: Resize images with optional aspect ratio preservation
- **Sketch Converter**: Transform photos into pencil sketch style
- **Background Eraser**: Remove black backgrounds from images
- **Cartoon Effect**: Apply cartoon/cartoon painting effects to images

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/JianliZh429/image-toolkit.git
cd image-toolkit

# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install opencv-python click

# Or install with poetry
poetry install
```

### Using pip (when published)

```bash
pip install image-toolkit
```

## Quick Start

### Using the Unified CLI

```bash
# Show all available commands
image-toolkit --help

# Resize an image
image-toolkit resize --image_file photo.jpg --width 800

# Convert to sketch
image-toolkit sketch --image_file photo.jpg

# Generate license photos
image-toolkit license-photo --image_file portrait.jpg --out_dir ./output
```

### Using Individual Scripts

```bash
# Each tool can also be run directly
python cli/resize.py --image_file photo.jpg --width 800
python cli/sketch.py --image_file photo.jpg
python cli/license_photo.py --image_file portrait.jpg
```

## Commands

### `license-photo`

Generate ID-style photos with different background colors (blue, red, white).

```bash
# ISO standard (35x45mm)
image-toolkit license-photo --image_file portrait.jpg --out_dir ./output

# US passport (2x2 inches / 600x600px)
image-toolkit license-photo --image_file portrait.jpg --country usa --doc-type passport

# UK visa (35x45mm)
image-toolkit license-photo --image_file portrait.jpg --country uk --doc-type visa

# Using common size alias
image-toolkit license-photo --image_file portrait.jpg --size us

# Legacy inch-based size
image-toolkit license-photo --image_file portrait.jpg --inch 1

# Custom dimensions
image-toolkit license-photo --image_file portrait.jpg --width 600 --height 600

# List available countries
image-toolkit license-photo --list-countries

# List document types for a country
image-toolkit license-photo --list-types usa
```

**Options:**
- `--image_file`: Path to input image (required for processing)
- `--out_dir`: Output directory (default: `./output`)
- `-c, --country`: Country code (e.g., `usa`, `uk`, `jp`, `cn`, `de`, `fr`). Default: `iso`
- `-d, --doc-type`: Document type (`passport`, `visa`, `id_card`, `iso_216`). Default: `iso_216`
- `-s, --size`: Common size alias (`iso`, `us`, `eu`, `uk`, `jp`, `cn`). Overrides country/doc-type
- `-i, --inch`: Legacy inch-based size (1 or 2). Overrides other size options
- `--width`, `--height`: Custom dimensions in pixels
- `--list-countries`: List all available country codes
- `--list-types`: List document types for a specific country
- `--verbose`: Show intermediate results (press ESC to close)

**Output:** Three images with different background colors:
- `blue.jpg` - Blue background (RGB: 61, 140, 221)
- `red.jpg` - Red background (RGB: 0, 0, 255)
- `white.jpg` - White background (RGB: 255, 255, 255)

**Supported Countries:** USA, Canada, UK, Germany, France, Spain, Italy, Netherlands, Sweden, Poland, Russia, China, Japan, South Korea, India, Singapore, Thailand, Vietnam, Philippines, Malaysia, Indonesia, UAE, Saudi Arabia, Israel, Turkey, Australia, New Zealand, Brazil, Argentina, Chile, Colombia, South Africa, Egypt, Nigeria, Kenya, and ISO standards.

---

### `resize`

Resize images to specified dimensions.

```bash
# Resize by width (height auto-calculated)
image-toolkit resize --image_file photo.jpg --width 1920

# Resize by height (width auto-calculated)
image-toolkit resize --image_file photo.jpg --height 1080

# Resize to exact dimensions
image-toolkit resize --image_file photo.jpg --width 800 --height 600
```

**Options:**
- `--image_file`: Path to input image (required)
- `--out_dir`: Output directory (default: `./output`)
- `--width`: Target width in pixels
- `--height`: Target height in pixels
- `--verbose`: Display resized image

**Note:** At least one of `--width` or `--height` must be specified.

---

### `sketch`

Convert images to pencil sketch style.

```bash
image-toolkit sketch --image_file photo.jpg --out_dir ./output
```

**Options:**
- `--image_file`: Path to input image (required)
- `--out_dir`: Output directory (default: `./output`)
- `--verbose`: Display sketch result

**Output:** PNG file with sketch effect applied.

---

### `black-bg-eraser`

Remove black backgrounds from images.

```bash
image-toolkit black-bg-eraser --image_file image.jpg --threshold 15
```

**Options:**
- `--image_file`: Path to input image (required)
- `--out_dir`: Output directory (default: `./output`)
- `--threshold`: Threshold value for binary thresholding (0-255, default: 10)
- `--margin`: Margin to crop from edges before processing (default: 0)
- `--verbose`: Display intermediate results

---

### `cartoonize`

Apply cartoon effect to images.

```bash
image-toolkit cartoonize --image_file photo.jpg --bilateral_filters 5
```

**Options:**
- `--image_file`: Path to input image (required)
- `--out_dir`: Output directory (default: `./output`)
- `--bilateral_filters`: Number of bilateral filter iterations (default: 4)
- `--verbose`: Display intermediate results

**Output:** Three images:
- `{name}_gray.jpg` - Grayscale version
- `{name}_sketch.jpg` - Edge sketch
- `{name}_painting.jpg` - Final cartoon painting

## Development

### Setup Development Environment

```bash
# Clone and setup
git clone https://github.com/JianliZh429/image-toolkit.git
cd image-toolkit
poetry install

# Or with virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=cli

# Run specific test file
pytest tests/test_resize.py
```

### Code Quality

```bash
# Format code
black cli/ tests/

# Check formatting
black --check cli/ tests/

# Lint
flake8 cli/ tests/

# Type checking
mypy cli/
```

## Project Structure

```
image-toolkit/
├── cli/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Unified CLI entry point
│   ├── files.py             # Utility functions
│   ├── license_photo.py     # License photo generator
│   ├── resize.py            # Image resizer
│   ├── sketch.py            # Sketch converter
│   ├── black_bg_eraser.py   # Background eraser
│   └── cartoonize.py        # Cartoon effect
├── tests/
│   ├── conftest.py          # Test fixtures
│   ├── test_files.py
│   ├── test_resize.py
│   ├── test_sketch.py
│   ├── test_license_photo.py
│   ├── test_black_bg_eraser.py
│   ├── test_cartoonize.py
│   └── test_main.py
├── docs/
│   └── DEVELOPMENT_PLAN.md
├── pyproject.toml
├── setup.cfg
└── README.md
```

## Requirements

- Python 3.7+
- OpenCV (opencv-python)
- Click

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## Acknowledgments

- Built with [OpenCV](https://opencv.org/)
- CLI powered by [Click](https://click.palletsprojects.com/)
