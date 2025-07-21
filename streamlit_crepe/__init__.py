"""
Streamlit Milkdown Crepe Component
==================================

A rich markdown editor component for Streamlit applications, powered by Milkdown Crepe.

This component provides a WYSIWYG markdown editor with advanced features including:
- Real-time markdown editing with live preview
- Mathematical formulas (LaTeX support)
- Code blocks with syntax highlighting  
- Interactive table editing
- Image upload with automatic compression
- Link editing with tooltips
- Standard markdown formatting

Quick Start
-----------
```python
import streamlit as st
from streamlit_crepe import st_milkdown

# Basic usage
content = st_milkdown("# Hello World")
st.write(content)

# With custom features
content = st_milkdown(
    default_value="# My Document",
    features={
        "math": True,      # LaTeX formulas
        "table": True,     # Table editing
        "image": True,     # Image uploads
        "codeblock": True, # Code blocks
        "link": True       # Link editing
    },
    height=400
)
```

Features Configuration
---------------------
The `features` parameter accepts a dictionary with the following keys:

- **codeblock** (bool): Enable code blocks with syntax highlighting
- **math** (bool): Enable LaTeX mathematical formulas ($...$ and $$...$$)
- **table** (bool): Enable interactive table creation and editing
- **image** (bool): Enable image upload with automatic compression (max 800px, 500KB)
- **link** (bool): Enable link editing with preview tooltips

All features are enabled by default. Set to False to disable specific features.

Image Handling
--------------
When image upload is enabled:
- Images are automatically compressed to maximum 800px width/height
- File size is reduced to maximum 500KB
- Images are embedded as base64 data URLs in the markdown
- Supports common formats: PNG, JPEG, GIF, WebP
- Processing is done asynchronously to avoid blocking the UI

Performance Notes
-----------------
- Use `throttle_delay` to control update frequency (default 250ms)
- Large documents may benefit from higher throttle delays
- Image compression happens in Web Workers for better performance
- The editor automatically adjusts height unless `height` is specified
"""

import os
from typing import Optional, Dict
import streamlit.components.v1 as components

__all__ = ["st_milkdown"]
__version__ = "0.1.0"

# Set this to False for development, True for production
_RELEASE = True

if not _RELEASE:
    # Development mode: use the local webpack dev server
    _component_func = components.declare_component(
        "streamlit_crepe",
        url="http://localhost:3001", 
    )
else:
    # Production mode: use the built frontend
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend", "build")
    _component_func = components.declare_component(
        "streamlit_crepe",
        path=build_dir
    )


def st_milkdown(
    default_value: str = "",
    height: Optional[int] = None,
    placeholder: str = "",
    readonly: bool = False,
    features: Optional[Dict[str, bool]] = None,
    throttle_delay: int = 250,
    key: Optional[str] = None
) -> str:
    """Create a Milkdown Crepe markdown editor component for Streamlit.
    
    This component provides a rich WYSIWYG markdown editor with support for:
    - Real-time markdown editing with live preview
    - Mathematical formulas (LaTeX)
    - Code blocks with syntax highlighting
    - Tables with interactive editing
    - Image upload with automatic compression (max 800px, 500KB)
    - Links with tooltips
    - Standard markdown formatting (bold, italic, lists, etc.)

    Parameters
    ----------
    default_value : str, default ""
        Initial markdown content to display in the editor.
        
    height : int, optional
        Fixed height of the editor in pixels. If None, the editor will
        automatically adjust its height based on content.
        
    placeholder : str, default ""
        Placeholder text shown when the editor is empty.
        
    readonly : bool, default False
        If True, the editor will be read-only and users cannot edit content.
        
    features : dict, optional
        Dictionary controlling which editor features are enabled.
        Available features:
        - "codeblock": Code blocks with syntax highlighting
        - "math": LaTeX mathematical formulas  
        - "table": Interactive table editing
        - "image": Image upload with automatic compression
        - "link": Link editing with tooltips
        
        Default: {"codeblock": True, "math": True, "table": True, "image": True, "link": True}
        
    throttle_delay : int, default 250
        Delay in milliseconds before sending editor changes to Streamlit.
        Higher values reduce update frequency but may feel less responsive.
        
    key : str, optional
        Unique key for the component. Use this when you have multiple
        editors on the same page to maintain separate state.

    Returns
    -------
    str
        The current markdown content from the editor.

    Examples
    --------
    Basic usage:
    
    >>> content = st_milkdown("# Hello World")
    >>> st.write(content)
    
    With custom features:
    
    >>> content = st_milkdown(
    ...     default_value="# My Document",
    ...     features={
    ...         "math": True,      # Enable LaTeX formulas
    ...         "table": True,     # Enable table editing
    ...         "image": False,    # Disable image uploads
    ...         "codeblock": True, # Enable code blocks
    ...         "link": True       # Enable link editing
    ...     },
    ...     height=400,
    ...     placeholder="Start writing your markdown..."
    ... )
    
    Read-only mode:
    
    >>> st_milkdown(
    ...     default_value="This content cannot be edited",
    ...     readonly=True
    ... )
    
    Multiple editors:
    
    >>> content1 = st_milkdown("# Editor 1", key="editor1")
    >>> content2 = st_milkdown("# Editor 2", key="editor2")

    Notes
    -----
    - Images are automatically compressed to max 800px width/height and 500KB size
    - All images are embedded as base64 data URLs in the markdown
    - The editor supports standard markdown syntax plus extensions
    - LaTeX formulas use $ for inline and $$ for block formulas
    - Tables can be edited interactively with mouse and keyboard
    - Code blocks support syntax highlighting for many languages
    """
    if features is None:
        features = {
            "codeblock": True,
            "math": True,
            "table": True,
            "image": True,
            "link": True,
        }
    
    component_value = _component_func(
        default_value=default_value,
        height=height,
        placeholder=placeholder,
        readonly=readonly,
        features=features,
        throttle_delay=throttle_delay,
        key=key,
    )

    return component_value or default_value
