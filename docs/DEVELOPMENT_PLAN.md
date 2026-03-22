# Development Plan - Image Toolkit

## Project Overview

**Image Toolkit** is a collection of image processing tools implemented using OpenCV. The project provides CLI-based utilities for common image manipulation tasks such as license photo generation, resizing, sketch conversion, background removal, and cartoon effects.

---

## Current State Analysis

### Architecture
- **Structure**: Single-module CLI tools in `cli/` directory
- **Dependencies**: OpenCV (opencv-python, opencv-contrib-python), Click for CLI
- **Build System**: Poetry
- **Python Version**: ^3.7

### Existing Tools
| Tool | File | Functionality |
|------|------|---------------|
| License Photo | `license_photo.py` | Extract person area and generate ID photos with blue/red/white backgrounds |
| Resize | `resize.py` | Resize images with optional aspect ratio preservation |
| Sketch | `sketch.py` | Convert images to sketch/pencil drawing style |
| Black BG Eraser | `black_bg_eraser.py` | Remove black backgrounds from images |
| Cartoonize | `cartoonize.py` | Apply cartoon/cartoon painting effects to images |

### Code Quality Observations
1. **Import inconsistencies**: Some files use relative imports (`from files import`), others use absolute imports
2. **Type hints**: Partial type hinting (some functions have them, others don't)
3. **Error handling**: Minimal error handling (no file existence checks, no exception handling)
4. **Testing**: No test suite present
5. **Documentation**: Basic docstrings only in `files.py`
6. **Code style**: Black configured but not consistently applied

---

## Development Roadmap

### Phase 1: Foundation & Code Quality (Priority: High)

#### 1.1 Fix Import System
- [ ] Convert all imports to consistent absolute imports
- [ ] Add `__init__.py` with proper package exports
- [ ] Create a CLI entry point for unified command access

#### 1.2 Add Error Handling
- [ ] Add file existence validation
- [ ] Add image format validation
- [ ] Add try-except blocks for OpenCV operations
- [ ] Add meaningful error messages

#### 1.3 Type Hints
- [ ] Add complete type hints to all functions
- [ ] Add return type annotations
- [ ] Consider using dataclasses for configuration

#### 1.4 Documentation
- [ ] Add comprehensive docstrings (Google/NumPy style)
- [ ] Document all parameters and return values
- [ ] Add usage examples in docstrings

---

### Phase 2: Testing Infrastructure (Priority: High)

#### 2.1 Test Framework Setup
- [ ] Add pytest as dev dependency
- [ ] Create test directory structure (`tests/`)
- [ ] Add test configuration (pytest.ini or pyproject.toml)

#### 2.2 Unit Tests
- [ ] Test `files.py` utility functions
- [ ] Test each CLI tool's core logic
- [ ] Test edge cases (empty images, invalid files, etc.)

#### 2.3 Integration Tests
- [ ] Create sample test images
- [ ] Test full CLI workflows
- [ ] Test output file generation

#### 2.4 CI/CD
- [ ] Add GitHub Actions workflow
- [ ] Configure automated testing on push/PR
- [ ] Add linting checks (flake8, black --check)

---

### Phase 3: CLI Improvements (Priority: Medium)

#### 3.1 Unified CLI Entry Point
- [ ] Create main CLI group with Click
- [ ] Add subcommands for each tool
- [ ] Implement `--version` and `--help` at root level

Example:
```bash
image-toolkit license-photo --image_file photo.jpg --out_dir ./output
image-toolkit resize --image_file photo.jpg --width 800
image-toolkit sketch --image_file photo.jpg
```

#### 3.2 Configuration Support
- [ ] Add config file support (YAML/TOML)
- [ ] Allow default values for common options
- [ ] Support environment variables

#### 3.3 Progress Indicators
- [ ] Add progress bars for long operations
- [ ] Add verbose/quiet modes
- [ ] Improve logging (use logging module)

---

### Phase 4: New Features (Priority: Medium)

#### 4.1 Additional Image Tools
- [ ] **Background Removal**: AI-powered background removal (e.g., using rembg)
- [ ] **Watermark**: Add text/image watermarks
- [ ] **Collage**: Create image collages/mosaics
- [ ] **Format Converter**: Batch convert between image formats
- [ ] **EXIF Editor**: View/edit image metadata
- [ ] **Filters**: Apply common filters (sepia, grayscale, etc.)

#### 4.2 Batch Processing
- [ ] Support multiple input files
- [ ] Add glob pattern support
- [ ] Parallel processing for batch operations

#### 4.3 GUI Option (Optional)
- [ ] Simple Tkinter/PyQt GUI for common operations
- [ ] Drag-and-drop support

---

### Phase 5: Performance & Optimization (Priority: Low)

#### 5.1 Performance Improvements
- [ ] Profile slow operations
- [ ] Add caching for repeated operations
- [ ] Optimize memory usage for large images

#### 5.2 Async Processing
- [ ] Consider asyncio for I/O-bound operations
- [ ] Add concurrent processing for batch operations

---

### Phase 6: Distribution & Packaging (Priority: Medium)

#### 6.1 Package Distribution
- [ ] Update pyproject.toml with proper entry points
- [ ] Publish to PyPI
- [ ] Add release workflow

#### 6.2 Binary Distribution
- [ ] Consider PyInstaller for standalone executables
- [ ] Create platform-specific builds

---

## Immediate Action Items (Next Sprint)

1. **Fix import inconsistencies** - Ensure all modules use consistent import style
2. **Add basic error handling** - File validation and exception handling
3. **Set up pytest** - Create initial test structure
4. **Add comprehensive docstrings** - Document all public functions
5. **Create unified CLI** - Single entry point for all tools

---

## Suggested Project Structure

```
image-toolkit/
├── cli/
│   ├── __init__.py
│   ├── main.py              # New: unified CLI entry point
│   ├── files.py
│   ├── license_photo.py
│   ├── resize.py
│   ├── sketch.py
│   ├── black_bg_eraser.py
│   └── cartoonize.py
├── core/                    # New: core processing logic
│   ├── __init__.py
│   ├── processors.py
│   └── config.py
├── tests/                   # New: test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_files.py
│   ├── test_license_photo.py
│   ├── test_resize.py
│   ├── test_sketch.py
│   ├── test_black_bg_eraser.py
│   └── test_cartoonize.py
├── docs/
│   ├── DEVELOPMENT_PLAN.md
│   ├── API.md
│   └── USAGE.md
├── samples/                 # New: sample images for testing
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Dependencies Recommendations

### Current
```toml
opencv-python = "^4.5.2"
opencv-contrib-python = "^4.5.2"
click = "^8.0.1"
```

### Suggested Additions (dev-dependencies)
```toml
pytest = "^7.0"
pytest-cov = "^4.0"
mypy = "^1.0"
```

### Suggested Additions (dependencies)
```toml
tqdm = "^4.65"        # Progress bars
rich = "^13.0"        # Rich CLI output
pillow = "^9.0"       # Additional image support
```

---

## Notes

- This plan is prioritized based on foundational needs first
- Phases can be adjusted based on user requirements
- Consider backward compatibility when making breaking changes
- Regular code reviews and refactoring should be part of ongoing development
