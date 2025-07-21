# Streamlit Crepe Component Documentation

## Overview

**Streamlit Crepe** is a custom component for Streamlit that integrates the modern Milkdown Crepe Markdown editor into Streamlit applications. The component provides a rich WYSIWYG interface for editing Markdown with support for tables, mathematical formulas, diagrams, and image uploads.

## Component Architecture

### General Structure

```
streamlit-crepe/
├── streamlit_crepe/              # Python package
│   ├── __init__.py              # Main component API
│   └── frontend/                # React/TypeScript frontend
│       ├── src/                 # Source code
│       │   ├── index.tsx        # React entry point
│       │   ├── CrepeEditor.tsx  # Main editor component
│       │   └── types.ts         # TypeScript types
│       ├── public/              # Static files
│       └── build/               # Built files
├── examples/                    # Usage examples
├── tests/                       # Tests
└── docs/                        # Documentation
```

### Technology Stack

**Backend (Python):**
- Streamlit Components API
- Python 3.7+

**Frontend (JavaScript/TypeScript):**
- React 18.3.1
- TypeScript 5.0.0
- Milkdown Crepe 7.5.0
- Parcel (bundler)
- Lodash.debounce (performance optimization)

## Main Components

### 1. Python API (`streamlit_crepe/__init__.py`)

#### `st_milkdown()` Function

Main function for creating an editor in Streamlit applications.

**Parameters:**
- `default_value: str` - Initial editor content
- `height: int` - Editor height in pixels (default `None`)
- `placeholder: str` - Placeholder text
- `readonly: bool` - Read-only mode
- `features: Dict[str, bool]` - Enabled editor features
- `throttle_delay: int` - Update delay in milliseconds (default 250)
- `key: str` - Unique component key

**Returns:** `str` - Markdown content from editor

#### Operating Modes

**Development Mode (`_RELEASE = False`):**
- Uses webpack dev server on `localhost:3001`
- Enables hot reload for development

**Production Mode (`_RELEASE = True`):**
- Uses built static files from `build/`
- Optimized for performance

### 2. React Component (`CrepeEditor.tsx`)

#### Main Features

1. **Milkdown Crepe Editor Initialization**
2. **Content Change Handling** with debouncing
3. **Fallback Mechanism** - simple textarea on errors
4. **Streamlit Integration** through ComponentProps API

#### Component Lifecycle

```typescript
useEffect(() => {
    // 1. Create Crepe instance
    const crepeInstance = new Crepe({
        root: editorRef.current,
        defaultValue: args.default_value || '',
    });

    // 2. Initialize editor
    crepeInstance.create().then(() => {
        // 3. Subscribe to changes
        crepeInstance.editor.onUpdate(() => {
            const markdown = crepeInstance.getMarkdown();
            debouncedSetComponentValue.current(markdown);
        });
        
        // 4. Notify Streamlit of readiness
        Streamlit.setComponentReady();
    });

    // 5. Cleanup on unmount
    return () => {
        crepeInstance.destroy();
    };
}, []);
```

### 3. Type System (`types.ts`)

```typescript
interface CrepeEditorProps extends ComponentProps {
    args: {
        value: string;
        height: number | string;
        placeholder: string;
        readonly: boolean;
        theme: string;
        features: Record<string, boolean>;
        toolbar: Record<string, boolean>;
    };
}
```

## Functionality

### Supported Editor Features

| Feature | Key | Description |
|---------|-----|-------------|
| Code blocks | `codeblock` | Code syntax highlighting |
| Diagrams | `diagram` | Mermaid diagrams |
| Emojis | `emoji` | Emoji support |
| Math | `math` | LaTeX formulas |
| Tables | `table` | Table editing |
| Images | `image` | Image insertion |
| Links | `link` | Hyperlinks |
| Upload | `upload` | File upload |

### Toolbar

| Button | Key | Function |
|--------|-----|----------|
| **B** | `bold` | Bold text |
| *I* | `italic` | Italic |
| ~~S~~ | `strike` | Strikethrough |
| `<>` | `code` | Inline code |
| H | `heading` | Headings |
| " | `quote` | Quotes |
| • | `list` | Lists |
| ⊞ | `table` | Tables |
| 🔗 | `link` | Links |
| 🖼️ | `image` | Images |
| {} | `codeblock` | Code blocks |

## Image Handling

Images are embedded directly in Markdown as data URLs:

```markdown
![alt text](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...)
```

**Advantages:**
- Simple implementation
- No external services required

**Disadvantages:**
- Increases document size
- May slow down performance with large images

## Performance Optimization

### Update Debouncing

The component uses debouncing to optimize update frequency:

```typescript
const debouncedSetComponentValue = useRef(
    debounce((markdown: string) => {
        Streamlit.setComponentValue(markdown);
    }, args.throttle_delay || 500)
);
```

**Delay Configuration:**
```python
st_milkdown(
    throttle_delay=1000,  # 1 second
    key="slow_editor"
)
```

### Memory Management

- Automatic resource cleanup on unmount
- Cancellation of pending debounced calls
- Proper Crepe instance destruction

## Error Handling

### Fallback Mechanism

On Milkdown Crepe initialization errors, the component automatically switches to a simple textarea:

```typescript
function createFallbackEditor() {
    const textarea = document.createElement('textarea');
    textarea.value = args.default_value || '';
    textarea.placeholder = args.placeholder || 'Enter markdown...';
    // ... style configuration
    
    textarea.addEventListener('input', (e) => {
        const value = (e.target as HTMLTextAreaElement).value;
        debouncedSetComponentValue.current(value);
    });
}
```

### Error Logging

All errors are logged to browser console for debugging:

```typescript
.catch(error => {
    console.error("Error creating Crepe editor:", error);
    createFallbackEditor();
});
```

## Streamlit Integration

### Component Lifecycle

1. **Initialization:** Streamlit creates iframe with React component
2. **Ready:** Component calls `Streamlit.setComponentReady()`
3. **Updates:** Changes are passed through `Streamlit.setComponentValue()`
4. **Size:** Height is set through `Streamlit.setFrameHeight()`

### Component State

Streamlit automatically manages component state:
- Preserves values between reruns
- Handles unique keys (`key` parameter)
- Synchronizes state between sessions

## Testing

### Test Structure

```
tests/
├── test_component.py      # Python API unit tests
└── test_integration.py    # Integration tests
```

### Test Coverage

**Python API Tests:**
- Module import
- Component declaration
- Basic function calls
- Parameter handling
- Callback functions
- Error handling

**Integration Tests:**
- Streamlit interaction
- Multiple editors
- Performance

### Running Tests

```bash
# All tests
pytest

# With code coverage
pytest --cov=streamlit_crepe

# Specific test
pytest tests/test_component.py::TestStreamlitCrepe::test_import
```

## Build and Deployment

### Build Process

1. **Frontend build:**
   ```bash
   cd streamlit_crepe/frontend
   npm install
   npm run build
   ```

2. **Python package:**
   ```bash
   python setup.py sdist bdist_wheel
   ```

### Automated Build

The `build_frontend.py` script automates the process:

```bash
python build_frontend.py
```

**What the script does:**
- Checks for Node.js and npm availability
- Installs dependencies
- Builds the project
- Verifies the result

## Usage Examples

### Basic Editor

```python
import streamlit as st
from streamlit_crepe import st_milkdown

content = st_milkdown(
    default_value="# Hello, World!",
    key="basic_editor"
)

st.markdown(content)
```

### Customized Editor

```python
content = st_milkdown(
    default_value="# My Editor",
    height=600,
    features={
        "math": True,
        "table": True,
        "diagram": False,  # Disable diagrams
    },
    toolbar={
        "bold": True,
        "italic": True,
        "heading": True,
        # Other buttons hidden
    },
    throttle_delay=1000,
    key="custom_editor"
)
```



## Limitations and Known Issues

### Current Limitations

1. **Image Size:** Large images in base64 mode may slow down performance
2. **Browser Compatibility:** Requires modern browsers with ES6+ support
3. **Mobile Devices:** Limited touch input support

### Known Issues

1. **Initialization:** Rare cases of failed Milkdown initialization
2. **Memory:** Possible memory leaks with frequent component recreation
3. **Performance:** Slowdown with very large documents (>10MB)

### Workarounds

1. **Fallback Mode:** Automatic switch to textarea
2. **Debouncing:** Update frequency optimization
3. **Cleanup:** Proper resource cleanup

## Development Roadmap

### Short-term Goals

- [ ] Improved mobile support
- [ ] Additional themes
- [ ] Plugins for specific formats
- [ ] Performance improvements

### Long-term Goals

- [ ] Collaborative editing
- [ ] Extended diagram support
- [ ] Cloud service integration
- [ ] Offline mode

## Conclusion

Streamlit Crepe is a powerful and flexible component for integrating modern Markdown editing into Streamlit applications. The component architecture provides:

- **Ease of use** through intuitive Python API
- **Configuration flexibility** through multiple parameters
- **Reliability** through fallback mechanisms
- **Performance** through optimizations and debouncing
- **Extensibility** for future improvements

The component is suitable for a wide range of applications: from simple text input forms to complex document management systems with support for mathematical formulas, diagrams, and multimedia content.