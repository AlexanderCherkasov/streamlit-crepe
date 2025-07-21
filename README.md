# Streamlit Crepe

[![PyPI version](https://badge.fury.io/py/streamlit-crepe.svg)](https://badge.fury.io/py/streamlit-crepe)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A rich markdown editor component for Streamlit applications, powered by Milkdown Crepe.

## ✨ Features

- 📝 **Rich WYSIWYG markdown editing** with live preview
- 🧮 **Mathematical formulas** with LaTeX support ($...$ and $$...$$)
- 💻 **Code blocks** with syntax highlighting for 100+ languages
- 📊 **Interactive tables** with mouse and keyboard editing
- 🖼️ **Image upload** with automatic compression (max 800px, 500KB)
- 🔗 **Smart links** with preview tooltips
- ⚡ **High performance** with Web Worker image processing
- 🎨 **Customizable features** - enable only what you need
- 📱 **Responsive design** with auto-height adjustment

## 🚀 Quick Start

### Installation

```bash
pip install streamlit-crepe
```

### Basic Usage

```python
import streamlit as st
from streamlit_crepe import st_milkdown

# Simple editor
content = st_milkdown("# Hello World")
st.write(content)
```

### Advanced Usage

```python
# Full-featured editor
content = st_milkdown(
    default_value="""# My Document

Write your **markdown** here with full feature support!

## Math
$E = mc^2$

## Code
```python
print("Hello, World!")
```

## Table
| Feature | Status |
|---------|--------|
| Math    | ✅     |
| Code    | ✅     |
| Tables  | ✅     |
""",
    height=400,
    features={
        "codeblock": True,  # Code blocks
        "math": True,       # LaTeX formulas  
        "table": True,      # Interactive tables
        "image": True,      # Image uploads
        "link": True        # Link editing
    },
    placeholder="Start writing your markdown...",
    throttle_delay=250
)

st.markdown(content)
```

## 📖 API Reference

### `st_milkdown()`

```python
st_milkdown(
    default_value: str = "",
    height: Optional[int] = None,
    placeholder: str = "",
    readonly: bool = False,
    features: Optional[Dict[str, bool]] = None,
    throttle_delay: int = 250,
    key: Optional[str] = None
) -> str
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `default_value` | `str` | `""` | Initial markdown content |
| `height` | `int` | `None` | Fixed height in pixels (auto if None) |
| `placeholder` | `str` | `""` | Placeholder text when empty |
| `readonly` | `bool` | `False` | Read-only mode |
| `features` | `dict` | See below | Feature configuration |
| `throttle_delay` | `int` | `250` | Update delay in milliseconds |
| `key` | `str` | `None` | Unique component key |

#### Default Features

```python
{
    "codeblock": True,   # Code blocks
    "math": True,        # LaTeX formulas
    "table": True,       # Interactive tables
    "image": True,       # Image uploads
    "link": True         # Link editing
}
```

## 🎛️ Feature Examples

### Math Editor
```python
st_milkdown(
    default_value="# Math Editor\n\n$\\int_0^1 x^2 dx = \\frac{1}{3}$",
    features={"math": True, "codeblock": False, "table": False, "image": False, "link": False}
)
```

### Code Editor
```python
st_milkdown(
    default_value="# Code Editor\n\n```python\nprint('Hello!')\n```",
    features={"codeblock": True, "math": False, "table": False, "image": False, "link": False}
)
```

### Simple Text Editor
```python
st_milkdown(
    default_value="# Simple Editor\n\nJust **basic** formatting.",
    features={"codeblock": False, "math": False, "table": False, "image": False, "link": True}
)
```

## 🖼️ Image Handling

Images are automatically processed for optimal performance:

- **Automatic compression** to max 800px width/height
- **Size optimization** to max 500KB file size
- **Format support**: PNG, JPEG, GIF, WebP
- **Base64 embedding** directly in markdown
- **Async processing** with Web Workers (no UI blocking)

## ⚡ Performance Tips

1. **Disable unused features** to reduce bundle size
2. **Use higher throttle_delay** for large documents (500-1000ms)
3. **Set fixed height** for consistent layout
4. **Use unique keys** for multiple editors

## 🔧 Development

### Requirements

- Python 3.7+
- Node.js 16+
- npm

### Setup

```bash
git clone https://github.com/yourusername/streamlit-crepe.git
cd streamlit-crepe
pip install -e .
python build_frontend.py
```

### Running Tests

```bash
python run_tests.py                    # All tests
python run_tests.py --browser          # Browser tests
python run_tests.py --manual           # Manual testing
```

### Building

```bash
python build_frontend.py              # Build frontend
python setup.py sdist bdist_wheel     # Create package
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Built on [Milkdown](https://milkdown.dev/) - A plugin-driven WYSIWYG markdown editor
- Uses [Crepe](https://github.com/Milkdown/crepe) - The official Milkdown editor component
- Image compression powered by [browser-image-compression](https://github.com/Donaldcwl/browser-image-compression)

