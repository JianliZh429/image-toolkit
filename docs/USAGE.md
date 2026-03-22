# Image Toolkit Usage Guide

Detailed usage examples for all Image Toolkit commands.

## Table of Contents

- [Installation](#installation)
- [License Photo](#license-photo)
- [Resize](#resize)
- [Sketch](#sketch)
- [Black Background Eraser](#black-background-eraser)
- [Cartoonize](#cartoonize)
- [Tips and Best Practices](#tips-and-best-practices)

---

## Installation

```bash
# Using pip
pip install opencv-python click

# Or using poetry
poetry install
```

---

## License Photo

Generate ID-style photos with standard backgrounds.

### Basic Usage

```bash
# Generate 1-inch license photos
image-toolkit license-photo --image_file portrait.jpg

# Generate 2-inch license photos
image-toolkit license-photo --image_file portrait.jpg --tz 2
```

### Output

Creates three files in `./output/`:
- `1_blue.jpg` - Blue background (RGB: 61, 140, 221)
- `1_red.jpg` - Red background (RGB: 0, 0, 255)
- `1_white.jpg` - White background (RGB: 255, 255, 255)

### Size Options

| Option | Dimensions | Use Case |
|--------|------------|----------|
| `--tz 1` | 295×413 px | 1 inch (standard ID) |
| `--tz 2` | 413×579 px | 2 inch (passport, certificates) |

### Custom Output Directory

```bash
image-toolkit license-photo --image_file portrait.jpg --out_dir ./id_photos
```

### Verbose Mode

```bash
# View the segmented result before saving
image-toolkit license-photo --image_file portrait.jpg --verbose 1
```

### Tips

- Use a clear, well-lit photo
- Ensure the subject is clearly separated from the background
- Higher resolution input images produce better results

---

## Resize

Resize images with flexible dimension options.

### Resize by Width (Preserve Aspect Ratio)

```bash
image-toolkit resize --image_file photo.jpg --width 1920
```

### Resize by Height (Preserve Aspect Ratio)

```bash
image-toolkit resize --image_file photo.jpg --height 1080
```

### Resize to Exact Dimensions

```bash
image-toolkit resize --image_file photo.jpg --width 800 --height 600
```

### Common Use Cases

```bash
# Social media profile picture (square)
image-toolkit resize --image_file photo.jpg --width 400 --height 400

# Full HD wallpaper
image-toolkit resize --image_file photo.jpg --width 1920 --height 1080

# Email attachment (reduce size)
image-toolkit resize --image_file photo.jpg --width 1024

# Thumbnail
image-toolkit resize --image_file photo.jpg --width 150
```

### Verbose Mode

```bash
# Preview the resized image
image-toolkit resize --image_file photo.jpg --width 800 --verbose 1
```

### Tips

- The tool automatically chooses the best interpolation method:
  - `INTER_AREA` for shrinking
  - `INTER_CUBIC` for enlarging
- Aspect ratio is preserved when only one dimension is specified

---

## Sketch

Convert photos to pencil sketch style.

### Basic Usage

```bash
image-toolkit sketch --image_file photo.jpg
```

### Output

Creates a PNG file: `{name}_png.png`

### Use Cases

```bash
# Create avatar from photo
image-toolkit sketch --image_file headshot.jpg --out_dir ./avatars

# Artistic effect for social media
image-toolkit sketch --image_file landscape.jpg --out_dir ./art
```

### Verbose Mode

```bash
# Preview the sketch result
image-toolkit sketch --image_file photo.jpg --verbose 1
```

### Tips

- Works best with clear, high-contrast images
- Portraits and landscapes produce striking results
- Output is grayscale PNG format

---

## Black Background Eraser

Remove black backgrounds from images.

### Basic Usage

```bash
image-toolkit black-bg-eraser --image_file image.jpg
```

### Adjust Threshold

```bash
# More aggressive background removal
image-toolkit black-bg-eraser --image_file image.jpg --threshold 20

# More conservative (keep more details)
image-toolkit black-bg-eraser --image_file image.jpg --threshold 5
```

### Add Margin Crop

```bash
# Crop 10 pixels from each edge before processing
image-toolkit black-bg-eraser --image_file image.jpg --margin 10
```

### Combined Options

```bash
image-toolkit black-bg-eraser --image_file scan.jpg --threshold 15 --margin 5
```

### Verbose Mode

```bash
# View threshold and result
image-toolkit black-bg-eraser --image_file image.jpg --verbose 1
```

### Tips

- Adjust `--threshold` based on your image:
  - Lower values: Keep more dark areas
  - Higher values: Remove more background
- Use `--margin` to remove scanner borders
- Works best when background is uniformly dark

---

## Cartoonize

Apply cartoon/cartoon painting effects.

### Basic Usage

```bash
image-toolkit cartoonize --image_file photo.jpg
```

### Output

Creates three files:
- `{name}_gray.jpg` - Grayscale version
- `{name}_sketch.jpg` - Edge sketch
- `{name}_painting.jpg` - Final cartoon painting

### Adjust Filter Strength

```bash
# Lighter effect (fewer filters)
image-toolkit cartoonize --image_file photo.jpg --bilateral_filters 2

# Stronger effect (more smoothing)
image-toolkit cartoonize --image_file photo.jpg --bilateral_filters 6
```

### Use Cases

```bash
# Create artistic profile picture
image-toolkit cartoonize --image_file selfie.jpg --out_dir ./art

# Generate multiple effect variations
image-toolkit cartoonize --image_file photo.jpg --bilateral_filters 4
```

### Verbose Mode

```bash
# View intermediate results
image-toolkit cartoonize --image_file photo.jpg --verbose 1
```

### Tips

- More bilateral filters = smoother, more cartoon-like
- Works well on portraits and simple scenes
- Complex scenes may lose detail with high filter counts

---

## Tips and Best Practices

### Image Quality

- Use high-resolution source images for best results
- Ensure good lighting and contrast
- Avoid heavily compressed images (artifacts may be amplified)

### Batch Processing

Process multiple images with a shell loop:

```bash
# Resize all JPGs in a directory
for img in *.jpg; do
    image-toolkit resize --image_file "$img" --width 1920
done

# Create sketches of all images
for img in *.jpg; do
    image-toolkit sketch --image_file "$img"
done
```

### Output Organization

```bash
# Organize outputs by tool
mkdir -p output/{resized,sketches,cartoons,id-photos}

image-toolkit resize --image_file photo.jpg --out_dir output/resized
image-toolkit sketch --image_file photo.jpg --out_dir output/sketches
```

### Performance

- Large images take longer to process
- Consider resizing large images before applying effects
- Close verbose windows with ESC key

### Error Handling

Common errors and solutions:

| Error | Solution |
|-------|----------|
| `Input image not found` | Check file path is correct |
| `Failed to read image` | Verify file is a valid image format |
| `No contours found` | Try adjusting threshold value |

---

## Getting Help

```bash
# General help
image-toolkit --help

# Command-specific help
image-toolkit resize --help
image-toolkit sketch --help
```

## Support

- Report bugs: [GitHub Issues](https://github.com/dew-maple/image-toolkit/issues)
- Documentation: [README.md](../README.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
