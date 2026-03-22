"""Tests for the photo_sizes module."""

import pytest

from cli.photo_sizes import (
    COMMON_SIZES,
    INCH_SIZES,
    PASSPORT_PHOTO_SIZES,
    get_common_size,
    get_inch_size,
    get_size,
    list_countries,
    list_document_types,
)


class TestGetSize:
    """Tests for get_size function."""

    def test_get_size_usa_passport(self) -> None:
        """Test US passport size."""
        assert get_size("usa", "passport") == (600, 600)

    def test_get_size_uk_passport(self) -> None:
        """Test UK passport size."""
        assert get_size("uk", "passport") == (413, 531)

    def test_get_size_iso(self) -> None:
        """Test ISO standard size."""
        assert get_size("iso", "iso_216") == (354, 472)

    def test_get_size_japan_passport(self) -> None:
        """Test Japan passport size."""
        assert get_size("japan", "passport") == (413, 531)

    def test_get_size_china_passport(self) -> None:
        """Test China passport size."""
        assert get_size("china", "passport") == (413, 531)

    def test_get_size_case_insensitive(self) -> None:
        """Test country and doc_type are case insensitive."""
        assert get_size("USA", "PASSPORT") == (600, 600)
        assert get_size("Uk", "Passport") == (413, 531)

    def test_get_size_invalid_country(self) -> None:
        """Test invalid country raises KeyError."""
        with pytest.raises(KeyError, match="Country 'invalid' not found"):
            get_size("invalid", "passport")

    def test_get_size_invalid_doc_type(self) -> None:
        """Test invalid document type raises KeyError."""
        with pytest.raises(KeyError, match="Document type 'invalid' not found"):
            get_size("usa", "invalid")


class TestGetCommonSize:
    """Tests for get_common_size function."""

    def test_get_common_size_iso(self) -> None:
        """Test ISO common size."""
        assert get_common_size("iso") == (354, 472)

    def test_get_common_size_us(self) -> None:
        """Test US common size."""
        assert get_common_size("us") == (600, 600)

    def test_get_common_size_eu(self) -> None:
        """Test EU common size."""
        assert get_common_size("eu") == (413, 531)

    def test_get_common_size_case_insensitive(self) -> None:
        """Test common size is case insensitive."""
        assert get_common_size("US") == (600, 600)
        assert get_common_size("Iso") == (354, 472)

    def test_get_common_size_invalid(self) -> None:
        """Test invalid common size raises KeyError."""
        with pytest.raises(KeyError, match="Common size 'invalid' not found"):
            get_common_size("invalid")


class TestGetInchSize:
    """Tests for get_inch_size function."""

    def test_get_inch_size_1(self) -> None:
        """Test 1 inch size."""
        assert get_inch_size(1) == (295, 413)

    def test_get_inch_size_2(self) -> None:
        """Test 2 inch size."""
        assert get_inch_size(2) == (413, 579)

    def test_get_inch_size_invalid(self) -> None:
        """Test invalid inch size raises KeyError."""
        with pytest.raises(KeyError, match="Inch size '3' not found"):
            get_inch_size(3)


class TestListCountries:
    """Tests for list_countries function."""

    def test_list_countries_returns_list(self) -> None:
        """Test list_countries returns a list."""
        countries = list_countries()
        assert isinstance(countries, list)
        assert len(countries) > 0

    def test_list_countries_sorted(self) -> None:
        """Test countries are sorted."""
        countries = list_countries()
        assert countries == sorted(countries)

    def test_list_countries_includes_major(self) -> None:
        """Test major countries are included."""
        countries = list_countries()
        assert "usa" in countries
        assert "uk" in countries
        assert "china" in countries
        assert "japan" in countries
        assert "iso" in countries


class TestListDocumentTypes:
    """Tests for list_document_types function."""

    def test_list_document_types_usa(self) -> None:
        """Test document types for USA."""
        types = list_document_types("usa")
        assert isinstance(types, list)
        assert "passport" in types
        assert "visa" in types

    def test_list_document_types_uk(self) -> None:
        """Test document types for UK."""
        types = list_document_types("uk")
        assert "passport" in types
        assert "visa" in types

    def test_list_document_types_sorted(self) -> None:
        """Test document types are sorted."""
        types = list_document_types("usa")
        assert types == sorted(types)

    def test_list_document_types_invalid_country(self) -> None:
        """Test invalid country raises KeyError."""
        with pytest.raises(KeyError, match="Country 'invalid' not found"):
            list_document_types("invalid")


class TestPhotoSizesData:
    """Tests for photo sizes data integrity."""

    def test_all_sizes_have_positive_dimensions(self) -> None:
        """Test all sizes have positive width and height."""
        for country, sizes in PASSPORT_PHOTO_SIZES.items():
            for doc_type, size in sizes.items():
                width, height = size
                assert width > 0, f"{country}/{doc_type} has invalid width"
                assert height > 0, f"{country}/{doc_type} has invalid height"

    def test_common_sizes_exist_in_countries(self) -> None:
        """Test common sizes correspond to actual country sizes."""
        # EU common size should match at least one European country
        eu_size = COMMON_SIZES["eu"]
        assert eu_size in [
            sizes.get("passport")
            for country, sizes in PASSPORT_PHOTO_SIZES.items()
            if country in ["germany", "france", "uk", "spain"]
        ]

    def test_inch_sizes_reasonable(self) -> None:
        """Test inch sizes are reasonable dimensions."""
        for inches, size in INCH_SIZES.items():
            width, height = size
            # At 300 DPI, 1 inch = 300 pixels approximately
            expected_min = inches * 250
            expected_max = inches * 350
            assert expected_min <= width <= expected_max or expected_min <= height <= expected_max
