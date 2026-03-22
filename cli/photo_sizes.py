"""International passport and ID photo size presets.

This module contains standard photo sizes for different countries
and document types (passport, visa, ID card, etc.).

All sizes are in pixels at 300 DPI (dots per inch).
"""

from typing import Dict, Tuple

# Photo size presets organized by country/region
# Format: (width_px, height_px) at 300 DPI
PASSPORT_PHOTO_SIZES: Dict[str, Dict[str, Tuple[int, int]]] = {
    # International Standards
    "iso": {
        "iso_216": (354, 472),  # 35x45mm (ISO/IEC 19794-5)
    },
    # North America
    "usa": {
        "passport": (600, 600),  # 2x2 inches (51x51mm)
        "visa": (600, 600),  # 2x2 inches (51x51mm)
        "green_card": (600, 750),  # 2x2.5 inches
    },
    "canada": {
        "passport": (413, 531),  # 35x45mm
        "pr_card": (413, 531),  # Permanent Resident card
    },
    "mexico": {
        "passport": (354, 472),  # 35x45mm
    },
    # Europe
    "uk": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "germany": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "france": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "spain": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm (DNI)
    },
    "italy": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    "netherlands": {
        "passport": (413, 531),  # 35x45mm
    },
    "sweden": {
        "passport": (413, 531),  # 35x45mm
    },
    "poland": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    "russia": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    # Asia
    "china": {
        "passport": (413, 531),  # 33x48mm
        "id_card": (354, 472),  # 32x26mm (smaller)
        "visa": (413, 531),  # 33x48mm
    },
    "japan": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
        "residence": (413, 531),  # 35x45mm
    },
    "south_korea": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    "india": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "singapore": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "thailand": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "vietnam": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "philippines": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "malaysia": {
        "passport": (413, 531),  # 35x50mm
    },
    "indonesia": {
        "passport": (413, 531),  # 35x45mm
    },
    # Middle East
    "uae": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "saudi_arabia": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "israel": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    "turkey": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    # Oceania
    "australia": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    "new_zealand": {
        "passport": (413, 531),  # 35x45mm
        "visa": (413, 531),  # 35x45mm
    },
    # South America
    "brazil": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm (RG)
    },
    "argentina": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm (DNI)
    },
    "chile": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    "colombia": {
        "passport": (413, 531),  # 35x45mm
        "id_card": (413, 531),  # 35x45mm
    },
    # Africa
    "south_africa": {
        "passport": (413, 531),  # 35x45mm
    },
    "egypt": {
        "passport": (413, 531),  # 35x45mm
    },
    "nigeria": {
        "passport": (413, 531),  # 35x45mm
    },
    "kenya": {
        "passport": (413, 531),  # 35x45mm
    },
}

# Common size aliases for quick access
COMMON_SIZES: Dict[str, Tuple[int, int]] = {
    "iso": (354, 472),  # 35x45mm ISO standard
    "us": (600, 600),  # 2x2 inches US standard
    "eu": (413, 531),  # 35x45mm European standard
    "uk": (413, 531),  # 35x45mm UK standard
    "jp": (413, 531),  # 35x45mm Japan standard
    "cn": (413, 531),  # 33x48mm China standard
}

# Legacy inch-based sizes (for backward compatibility)
INCH_SIZES: Dict[int, Tuple[int, int]] = {
    1: (295, 413),  # 1 inch (25x35mm approx)
    2: (413, 579),  # 2 inch (35x49mm approx)
}


def get_size(country: str = "iso", doc_type: str = "passport") -> Tuple[int, int]:
    """Get photo size for a specific country and document type.

    Args:
        country: Country code (e.g., 'usa', 'uk', 'jp') or 'iso' for ISO standard.
        doc_type: Document type (e.g., 'passport', 'visa', 'id_card').

    Returns:
        Tuple of (width_px, height_px) at 300 DPI.

    Raises:
        KeyError: If country or document type is not found.

    Examples:
        >>> get_size("usa", "passport")
        (600, 600)
        >>> get_size("uk", "passport")
        (413, 531)
        >>> get_size("iso", "iso_216")
        (354, 472)
    """
    country_lower = country.lower()
    doc_type_lower = doc_type.lower()

    if country_lower not in PASSPORT_PHOTO_SIZES:
        raise KeyError(
            f"Country '{country}' not found. " f"Available countries: {', '.join(PASSPORT_PHOTO_SIZES.keys())}"
        )

    country_sizes = PASSPORT_PHOTO_SIZES[country_lower]

    if doc_type_lower not in country_sizes:
        available = ", ".join(country_sizes.keys())
        raise KeyError(
            f"Document type '{doc_type}' not found for country '{country}'. " f"Available types: {available}"
        )

    return country_sizes[doc_type_lower]


def get_common_size(name: str) -> Tuple[int, int]:
    """Get size by common alias.

    Args:
        name: Common size alias (e.g., 'iso', 'us', 'eu').

    Returns:
        Tuple of (width_px, height_px) at 300 DPI.

    Raises:
        KeyError: If alias is not found.
    """
    name_lower = name.lower()
    if name_lower not in COMMON_SIZES:
        raise KeyError(f"Common size '{name}' not found. " f"Available: {', '.join(COMMON_SIZES.keys())}")
    return COMMON_SIZES[name_lower]


def get_inch_size(inches: int) -> Tuple[int, int]:
    """Get legacy inch-based size.

    Args:
        inches: Size in inches (1 or 2).

    Returns:
        Tuple of (width_px, height_px) at 300 DPI.

    Raises:
        KeyError: If inch size is not found.
    """
    if inches not in INCH_SIZES:
        raise KeyError(f"Inch size '{inches}' not found. Available: 1, 2")
    return INCH_SIZES[inches]


def list_countries() -> list:
    """List all available country codes.

    Returns:
        List of country codes.
    """
    return sorted(PASSPORT_PHOTO_SIZES.keys())


def list_document_types(country: str) -> list:
    """List available document types for a country.

    Args:
        country: Country code.

    Returns:
        List of document types for the country.

    Raises:
        KeyError: If country is not found.
    """
    country_lower = country.lower()
    if country_lower not in PASSPORT_PHOTO_SIZES:
        raise KeyError(
            f"Country '{country}' not found. " f"Available countries: {', '.join(PASSPORT_PHOTO_SIZES.keys())}"
        )
    return sorted(PASSPORT_PHOTO_SIZES[country_lower].keys())
