"""Basic image tests for streamlit-crepe"""
import pytest
from unittest.mock import patch
from streamlit_crepe import st_milkdown


@patch('streamlit_crepe._component_func')
def test_image_in_markdown(mock_component):
    """Test markdown with base64 image"""
    test_markdown = "# Test\n\n![Image](data:image/png;base64,test)"
    mock_component.return_value = test_markdown
    
    result = st_milkdown()
    assert result == test_markdown
    assert "data:image/png;base64" in result


@patch('streamlit_crepe._component_func')
def test_image_feature_enabled(mock_component):
    """Test with image feature enabled"""
    mock_component.return_value = "# Test"
    
    result = st_milkdown(features={"image": True})
    assert result == "# Test"


@patch('streamlit_crepe._component_func')
def test_image_feature_disabled(mock_component):
    """Test with image feature disabled"""
    mock_component.return_value = "# Test"
    
    result = st_milkdown(features={"image": False})
    assert result == "# Test"