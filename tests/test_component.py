"""Basic tests for streamlit-crepe component"""
import pytest
from unittest.mock import patch
from streamlit_crepe import st_milkdown


def test_import():
    """Test module import"""
    assert callable(st_milkdown)


@patch('streamlit_crepe._component_func')
def test_basic_call(mock_component):
    """Test basic component call"""
    mock_component.return_value = "# Test"
    result = st_milkdown("# Hello")
    assert result == "# Test"


@patch('streamlit_crepe._component_func')
def test_with_features(mock_component):
    """Test with features"""
    mock_component.return_value = "# Test"
    result = st_milkdown(
        default_value="# Hello",
        features={"math": True, "image": False}
    )
    assert result == "# Test"


@patch('streamlit_crepe._component_func')
def test_fallback_value(mock_component):
    """Test fallback to default"""
    mock_component.return_value = None
    result = st_milkdown(default_value="# Default")
    assert result == "# Default"