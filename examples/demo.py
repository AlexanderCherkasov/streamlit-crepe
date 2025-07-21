import streamlit as st

# Set page config must be the first Streamlit command
st.set_page_config(page_title="Streamlit Milkdown Demo", layout="wide")

from streamlit_crepe import st_milkdown

st.title("Streamlit Milkdown Crepe Demo")


# Editor settings from sidebar
st.sidebar.title("Editor Settings")
readonly = st.sidebar.checkbox("Read-only", value=False)

# Auto height setting
auto_height = st.sidebar.checkbox("Auto height (use content height)", value=True)
height = None if auto_height else st.sidebar.slider("Editor height", min_value=200, max_value=800, value=600, step=50)
throttle_delay = st.sidebar.slider("Throttle Delay (ms)", min_value=100, max_value=2000, value=500, step=50)

# Feature toggles
st.sidebar.subheader("Features")
features = {
    "codeblock": st.sidebar.checkbox("Code blocks", value=True),
    "math": st.sidebar.checkbox("Math formulas", value=True),
    "table": st.sidebar.checkbox("Tables", value=True),
    "image": st.sidebar.checkbox("Images", value=True),
    "link": st.sidebar.checkbox("Links", value=True),
}

# No upload callback needed - images are embedded as base64 directly

# Debug: Show what features are being passed
st.sidebar.write("**Debug - Features being passed:**")
st.sidebar.json(features)

# Layout: editor and preview side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Markdown Editor")
    # Create a unique key based on features to force recreation
    import hashlib
    import json
    features_key = hashlib.md5(json.dumps(features, sort_keys=True).encode()).hexdigest()[:8]
    
    content = st_milkdown(
        default_value=r"""# Welcome to Milkdown Crepe!

## Editor Features

* **Bold text** and *italics*
* ~~Strikethrough~~
* `Inline code`
* Support for [links](https://milkdown.dev/)

> Blockquotes are supported too

### Math Formulas

$
e^{i\pi} + 1 = 0
$

### Tables

| Header 1 | Header 2 |
|:-------------|:-------------|
| Cell 1    | Cell 2    |
| Cell 3    | Cell 4    |

### Images

Upload images using the image button in the toolbar - they will be embedded as base64 directly in the markdown!
""",
        placeholder="Start typing...",
        height=height,
        readonly=readonly,
        features=features,
        throttle_delay=throttle_delay,
        key=f"editor_{features_key}"
    )

# Results column
with col2:
    st.subheader("Markdown Output")
   # st.code(content, language="markdown")
    
    #st.subheader("Rendered Output")
    st.markdown(content)
    
    # Display image if uploaded (this part might need adjustment based on how image data is returned)
    # if isinstance(content, dict) and "image_data" in content:
    #     st.subheader("Uploaded Image")
    #     st.image(content["image_data"], caption=content.get("image_name", "Uploaded image"))

if st.sidebar.button("Update Settings"):
    st.rerun()

