"""Basic integration tests"""
import pytest
from unittest.mock import patch
from streamlit_crepe import st_milkdown


@patch('streamlit_crepe._component_func')
def test_multiple_editors(mock_component):
    """Test multiple editors"""
    mock_component.side_effect = ["# Editor 1", "# Editor 2"]
    
    result1 = st_milkdown(key="editor_1")
    result2 = st_milkdown(key="editor_2")
    
    assert result1 == "# Editor 1"
    assert result2 == "# Editor 2"
    assert mock_component.call_count == 2


@patch('streamlit_crepe._component_func')
def test_throttle_delay(mock_component):
    """Test throttle delay parameter"""
    mock_component.return_value = "# Test"
    
    st_milkdown(throttle_delay=500, key="throttle_test")
    
    call_args = mock_component.call_args[1]
    assert call_args['throttle_delay'] == 500