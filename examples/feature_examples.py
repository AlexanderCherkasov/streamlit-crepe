"""
Streamlit Crepe Feature Configuration Examples
==============================================

This file demonstrates different feature configurations for the st_milkdown component.
"""

import streamlit as st
from streamlit_crepe import st_milkdown

st.set_page_config(page_title="Feature Examples", layout="wide")

st.title("🎛️ Streamlit Crepe Feature Examples")
st.markdown("---")

# Example 1: All Features Enabled (Default)
st.subheader("1. All Features Enabled (Default)")
st.code("""
content = st_milkdown(
    default_value="# Full-Featured Editor",
    features={
        "codeblock": True,  # Code blocks with syntax highlighting
        "math": True,       # LaTeX mathematical formulas
        "table": True,      # Interactive table editing
        "image": True,      # Image upload with compression
        "link": True        # Link editing with tooltips
    }
)
""", language="python")

content1 = st_milkdown(
    default_value="""# Full-Featured Editor

This editor has all features enabled:

## Code Blocks
```python
def hello_world():
    print("Hello, World!")
```

## Math Formulas
Inline: $E = mc^2$

Block:
$$
\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}
$$

## Tables
| Feature | Enabled |
|---------|---------|
| Code    | ✅      |
| Math    | ✅      |
| Tables  | ✅      |
| Images  | ✅      |
| Links   | ✅      |

## Images
Upload images using the toolbar button above!

## Links
Check out [Milkdown](https://milkdown.dev/) for more info.
""",
    features={
        "codeblock": True,
        "math": True,
        "table": True,
        "image": True,
        "link": True
    },
    height=300,
    key="full_features"
)

st.markdown("---")

# Example 2: Math-Only Editor
st.subheader("2. Math-Only Editor")
st.code("""
content = st_milkdown(
    default_value="# Math Editor",
    features={
        "codeblock": False,
        "math": True,       # Only math enabled
        "table": False,
        "image": False,
        "link": False
    }
)
""", language="python")

content2 = st_milkdown(
    default_value="""# Math Editor

This editor is optimized for mathematical content:

Inline formulas: $\\alpha + \\beta = \\gamma$

Block formulas:
$$
\\frac{d}{dx}\\left( \\int_{0}^{x} f(u)\\,du\\right) = f(x)
$$

Quadratic formula:
$$
x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}
$$
""",
    features={
        "codeblock": False,
        "math": True,
        "table": False,
        "image": False,
        "link": False
    },
    height=250,
    key="math_only"
)

st.markdown("---")

# Example 3: Code-Only Editor
st.subheader("3. Code-Only Editor")
st.code("""
content = st_milkdown(
    default_value="# Code Editor",
    features={
        "codeblock": True,  # Only code blocks enabled
        "math": False,
        "table": False,
        "image": False,
        "link": False
    }
)
""", language="python")

content3 = st_milkdown(
    default_value="""# Code Editor

This editor is optimized for code documentation:

```python
# Python example
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])
```

```javascript
// JavaScript example
const factorial = (n) => {
    return n <= 1 ? 1 : n * factorial(n - 1);
};

console.log(factorial(5)); // 120
```

```sql
-- SQL example
SELECT users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id
ORDER BY order_count DESC;
```
""",
    features={
        "codeblock": True,
        "math": False,
        "table": False,
        "image": False,
        "link": False
    },
    height=300,
    key="code_only"
)

st.markdown("---")

# Example 4: Simple Text Editor
st.subheader("4. Simple Text Editor")
st.code("""
content = st_milkdown(
    default_value="# Simple Editor",
    features={
        "codeblock": False,
        "math": False,
        "table": False,
        "image": False,
        "link": True        # Only basic text + links
    }
)
""", language="python")

content4 = st_milkdown(
    default_value="""# Simple Text Editor

This is a minimal editor with only basic formatting:

- **Bold text**
- *Italic text*
- ~~Strikethrough~~
- `Inline code`

> Blockquotes work too

1. Numbered lists
2. Are supported
3. As well

And you can add [links](https://streamlit.io) to external sites.

Perfect for simple note-taking or basic documentation!
""",
    features={
        "codeblock": False,
        "math": False,
        "table": False,
        "image": False,
        "link": True
    },
    height=250,
    key="simple_text"
)

st.markdown("---")

# Example 5: Table-Focused Editor
st.subheader("5. Table-Focused Editor")
st.code("""
content = st_milkdown(
    default_value="# Table Editor",
    features={
        "codeblock": False,
        "math": False,
        "table": True,      # Focus on tables
        "image": False,
        "link": True
    }
)
""", language="python")

content5 = st_milkdown(
    default_value="""# Table Editor

This editor is optimized for creating and editing tables:

## Product Comparison

| Product | Price | Rating | Available |
|---------|-------|--------|-----------|
| Widget A | $29.99 | ⭐⭐⭐⭐⭐ | ✅ |
| Widget B | $39.99 | ⭐⭐⭐⭐ | ✅ |
| Widget C | $19.99 | ⭐⭐⭐ | ❌ |

## Team Members

| Name | Role | Email | Status |
|------|------|-------|--------|
| Alice | Developer | alice@company.com | Active |
| Bob | Designer | bob@company.com | Active |
| Carol | Manager | carol@company.com | On Leave |

Click on any cell to edit the table content!
""",
    features={
        "codeblock": False,
        "math": False,
        "table": True,
        "image": False,
        "link": True
    },
    height=300,
    key="table_focused"
)

st.markdown("---")

# Show all outputs
st.subheader("📄 Editor Outputs")

col1, col2 = st.columns(2)

with col1:
    st.write("**Full Features:**")
    st.code(content1[:200] + "..." if len(content1) > 200 else content1, language="markdown")
    
    st.write("**Math Only:**")
    st.code(content2[:200] + "..." if len(content2) > 200 else content2, language="markdown")
    
    st.write("**Simple Text:**")
    st.code(content4[:200] + "..." if len(content4) > 200 else content4, language="markdown")

with col2:
    st.write("**Code Only:**")
    st.code(content3[:200] + "..." if len(content3) > 200 else content3, language="markdown")
    
    st.write("**Table Focused:**")
    st.code(content5[:200] + "..." if len(content5) > 200 else content5, language="markdown")

# Configuration reference
st.markdown("---")
st.subheader("🔧 Feature Configuration Reference")

st.markdown("""
### Available Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| `codeblock` | Code blocks with syntax highlighting | Technical documentation, tutorials |
| `math` | LaTeX mathematical formulas | Scientific papers, equations |
| `table` | Interactive table editing | Data presentation, comparisons |
| `image` | Image upload with compression | Visual content, screenshots |
| `link` | Link editing with tooltips | References, external resources |

### Performance Tips

- **Disable unused features** to reduce bundle size and improve performance
- **Use higher `throttle_delay`** for large documents (500-1000ms)
- **Set fixed `height`** for consistent layout in complex apps
- **Use unique `key`** for multiple editors on the same page

### Common Configurations

```python
# Documentation site
features = {"codeblock": True, "math": False, "table": True, "image": True, "link": True}

# Scientific writing
features = {"codeblock": False, "math": True, "table": True, "image": True, "link": True}

# Simple note-taking
features = {"codeblock": False, "math": False, "table": False, "image": False, "link": True}

# Code tutorials
features = {"codeblock": True, "math": False, "table": False, "image": True, "link": True}
```
""")