import streamlit as st
from streamlit_crepe import st_milkdown

st.title("🔤 Placeholder Text Test")

st.markdown("""
Этот тест проверяет функциональность placeholder text в компоненте.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Без placeholder")
    content1 = st_milkdown(
        default_value="",
        placeholder="",
        key="no_placeholder"
    )

with col2:
    st.subheader("С custom placeholder")
    content2 = st_milkdown(
        default_value="",
        placeholder="Начните писать ваш markdown здесь...",
        key="with_placeholder"
    )

st.subheader("Разные варианты placeholder")

# Тест с разными placeholder текстами
placeholders = [
    "Start typing...",
    "Введите ваш текст здесь",
    "📝 Write your markdown content",
    "Empty editor - click to start writing",
    "Placeholder with emoji 🚀✨📚"
]

for i, placeholder_text in enumerate(placeholders):
    st.markdown(f"**Placeholder {i+1}:** `{placeholder_text}`")
    content = st_milkdown(
        default_value="",
        placeholder=placeholder_text,
        height=150,
        key=f"placeholder_{i}"
    )
    if content:
        st.code(content[:100] + "..." if len(content) > 100 else content)

st.subheader("Тест с features")
st.markdown("Placeholder с отключенными features:")

content_features = st_milkdown(
    default_value="",
    placeholder="Только базовый текст (все features отключены)",
    features={
        "codeblock": False,
        "math": False,
        "table": False,
        "image": False,
        "link": False,
    },
    key="placeholder_no_features"
)

st.subheader("Результаты")
st.json({
    "content1": content1[:50] + "..." if len(content1) > 50 else content1,
    "content2": content2[:50] + "..." if len(content2) > 50 else content2,
    "content_features": content_features[:50] + "..." if len(content_features) > 50 else content_features,
})