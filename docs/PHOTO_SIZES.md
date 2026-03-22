# International Photo Size Presets

This document lists all supported passport and ID photo sizes by country.

## Overview

Image Toolkit supports **40+ countries** with standard passport, visa, and ID card photo sizes. All sizes are specified in pixels at **300 DPI** (dots per inch).

## Quick Reference

| Country/Region | Code | Passport Size | Common Use |
|---------------|------|---------------|------------|
| ISO Standard | `iso` | 354×472 px | 35×45mm international |
| USA | `usa` | 600×600 px | 2×2 inches |
| UK | `uk` | 413×531 px | 35×45mm |
| European Union | `eu` | 413×531 px | 35×45mm |
| Japan | `jp` | 413×531 px | 35×45mm |
| China | `cn` | 413×531 px | 33×48mm |

## Usage Examples

### Basic Usage

```bash
# Default ISO standard (35×45mm)
image-toolkit license-photo --image_file photo.jpg

# US passport (2×2 inches)
image-toolkit license-photo --image_file photo.jpg --country usa --doc-type passport

# UK visa
image-toolkit license-photo --image_file photo.jpg --country uk --doc-type visa

# Common size alias (US)
image-toolkit license-photo --image_file photo.jpg --size us
```

### List Available Options

```bash
# List all country codes
image-toolkit license-photo --list-countries

# List document types for USA
image-toolkit license-photo --list-types usa
```

## Supported Countries and Sizes

### North America

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **USA** | passport | 600×600 | 51×51 (2×2") |
| | visa | 600×600 | 51×51 (2×2") |
| | green_card | 600×750 | 51×64 (2×2.5") |
| **Canada** | passport | 413×531 | 35×45mm |
| | pr_card | 413×531 | 35×45mm |
| **Mexico** | passport | 354×472 | 35×45mm |

### Europe

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **UK** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Germany** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **France** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Spain** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **Italy** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **Netherlands** | passport | 413×531 | 35×45mm |
| **Sweden** | passport | 413×531 | 35×45mm |
| **Poland** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **Russia** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |

### Asia

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **China** | passport | 413×531 | 33×48mm |
| | id_card | 354×472 | 32×26mm |
| | visa | 413×531 | 33×48mm |
| **Japan** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| | residence | 413×531 | 35×45mm |
| **South Korea** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **India** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Singapore** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Thailand** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Vietnam** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Philippines** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Malaysia** | passport | 413×531 | 35×50mm |
| **Indonesia** | passport | 413×531 | 35×45mm |

### Middle East

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **UAE** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Saudi Arabia** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **Israel** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **Turkey** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |

### Oceania

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **Australia** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |
| **New Zealand** | passport | 413×531 | 35×45mm |
| | visa | 413×531 | 35×45mm |

### South America

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **Brazil** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm (RG) |
| **Argentina** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm (DNI) |
| **Chile** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |
| **Colombia** | passport | 413×531 | 35×45mm |
| | id_card | 413×531 | 35×45mm |

### Africa

| Country | Document Type | Size (pixels) | Size (mm) |
|---------|--------------|---------------|-----------|
| **South Africa** | passport | 413×531 | 35×45mm |
| **Egypt** | passport | 413×531 | 35×45mm |
| **Nigeria** | passport | 413×531 | 35×45mm |
| **Kenya** | passport | 413×531 | 35×45mm |

## Common Size Aliases

For convenience, you can use these common size aliases:

| Alias | Size (pixels) | Description |
|-------|---------------|-------------|
| `iso` | 354×472 | ISO/IEC 19794-5 (35×45mm) |
| `us` | 600×600 | US Standard (2×2 inches) |
| `eu` | 413×531 | European Standard (35×45mm) |
| `uk` | 413×531 | UK Standard (35×45mm) |
| `jp` | 413×531 | Japan Standard (35×45mm) |
| `cn` | 413×531 | China Standard (33×48mm) |

## Legacy Inch-Based Sizes

For backward compatibility, inch-based sizes are still supported:

| Inches | Size (pixels) | Approximate mm |
|--------|---------------|----------------|
| 1 | 295×413 | 25×35mm |
| 2 | 413×579 | 35×49mm |

```bash
# Use legacy 1-inch size
image-toolkit license-photo --image_file photo.jpg --inch 1

# Use legacy 2-inch size
image-toolkit license-photo --image_file photo.jpg --inch 2
```

## Custom Sizes

You can specify custom dimensions in pixels:

```bash
# Custom 500×700 pixels
image-toolkit license-photo --image_file photo.jpg --width 500 --height 700
```

## Technical Notes

- All sizes are specified at **300 DPI** (dots per inch)
- The tool automatically resizes your image to the target dimensions
- Output images are saved with three background colors: blue, red, and white
- For best results, use high-resolution source images

## Sources

- ISO/IEC 19794-5:2011 (International standard)
- U.S. Department of State
- UK Passport Office
- European Union passport standards
- Individual country immigration/passport offices

## Contributing

If you find incorrect sizes or want to add more countries, please open an issue or submit a pull request.
