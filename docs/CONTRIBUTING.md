# Contributing to Image Toolkit

Thank you for considering contributing to Image Toolkit! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/image-toolkit.git
   cd image-toolkit
   ```
3. **Set up the development environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install opencv-python click pytest pytest-cov black flake8 mypy
   ```
4. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Making Changes

1. Make your changes to the codebase
2. Ensure all imports are absolute (from cli import ...)
3. Add type hints to all functions
4. Add docstrings to all public functions (Google style)
5. Write tests for new functionality

### Code Style

We follow these coding standards:

- **Formatting**: Black with 120 character line length
- **Linting**: Flake8
- **Type Checking**: Mypy
- **Imports**: Absolute imports from cli package
- **Docstrings**: Google style

```python
"""Module description."""

from cli.files import cv2_save


def process_image(image_file: str, out_dir: str) -> str:
    """Process an image and save the result.

    Args:
        image_file: Path to the input image file.
        out_dir: Directory to save the output.

    Returns:
        Path to the saved output file.

    Raises:
        FileNotFoundError: If the input file does not exist.
    """
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"Input not found: {image_file}")
    
    # Implementation...
    return output_path
```

### Running Quality Checks

Before submitting a PR, ensure all checks pass:

```bash
# Format code
black cli/ tests/

# Check formatting
black --check cli/ tests/

# Lint
flake8 cli/ tests/

# Type check
mypy cli/ --ignore-missing-imports

# Run tests
pytest
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use pytest fixtures from `conftest.py`
- Aim for high test coverage

Example test:

```python
def test_resize_width_only(sample_image_file: str, temp_dir: str) -> None:
    """Test resizing with width only."""
    runner = CliRunner()
    result = runner.invoke(
        resize,
        ["--image_file", sample_image_file, "--out_dir", temp_dir, "--width", "50"],
    )
    assert result.exit_code == 0
    assert "Resized image saved to" in result.output
```

## Pull Request Process

1. **Update documentation** if you change functionality
2. **Add tests** for new features
3. **Ensure all checks pass** (black, flake8, mypy, pytest)
4. **Update CHANGELOG** if applicable
5. **Submit PR** with a clear description of changes

### PR Checklist

- [ ] Code follows style guidelines (black, flake8)
- [ ] Type hints are complete (mypy passes)
- [ ] Tests pass (pytest)
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive

## Commit Messages

Follow conventional commit format:

```
feat: add new cartoon effect option
fix: resolve image read error on Windows
docs: update installation instructions
test: add tests for resize module
refactor: simplify grab_cut function
```

## Reporting Issues

### Bug Reports

Include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages and stack traces

### Feature Requests

Include:
- Description of the feature
- Use case
- Example usage

## Questions?

Open an issue for any questions or discussions.

## Thank You!

Your contributions make Image Toolkit better for everyone! 🎉
