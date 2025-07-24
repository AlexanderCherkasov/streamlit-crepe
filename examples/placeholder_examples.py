"""
Примеры использования placeholder text в Streamlit Crepe компоненте
"""

import streamlit as st
from streamlit_crepe import st_milkdown

st.set_page_config(page_title="Placeholder Examples", layout="wide")

st.title("🔤 Примеры Placeholder Text")

st.markdown("""
Этот пример показывает различные способы использования placeholder text в компоненте Streamlit Crepe.
""")

# Базовый пример
st.subheader("1. Базовое использование")
st.code('''
content = st_milkdown(
    placeholder="Начните писать ваш markdown...",
    key="basic_example"
)
''')

content_basic = st_milkdown(
    placeholder="Начните писать ваш markdown...",
    key="basic_example"
)

# Пример с разными языками
st.subheader("2. Многоязычные placeholder")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Русский**")
    content_ru = st_milkdown(
        placeholder="Введите ваш текст здесь...",
        height=200,
        key="placeholder_ru"
    )

with col2:
    st.markdown("**English**")
    content_en = st_milkdown(
        placeholder="Start typing your content here...",
        height=200,
        key="placeholder_en"
    )

with col3:
    st.markdown("**Español**")
    content_es = st_milkdown(
        placeholder="Comience a escribir su contenido aquí...",
        height=200,
        key="placeholder_es"
    )

# Пример с emoji и специальными символами
st.subheader("3. Placeholder с emoji и символами")

emoji_examples = [
    ("📝 Заметки", "📝 Напишите ваши заметки здесь..."),
    ("📚 Документация", "📚 Создайте документацию для вашего проекта"),
    ("✍️ Блог", "✍️ Поделитесь своими мыслями и идеями"),
    ("🚀 README", "🚀 Опишите ваш проект и как его использовать"),
    ("💡 Идеи", "💡 Запишите ваши креативные идеи"),
]

for title, placeholder_text in emoji_examples:
    with st.expander(title):
        content = st_milkdown(
            placeholder=placeholder_text,
            height=150,
            key=f"emoji_{title.replace(' ', '_')}"
        )
        if content:
            st.markdown("**Содержимое:**")
            st.code(content[:100] + "..." if len(content) > 100 else content)

# Пример с контекстными placeholder для разных features
st.subheader("4. Контекстные placeholder для разных features")

feature_examples = [
    {
        "title": "Математические формулы",
        "placeholder": "Введите текст с формулами... Используйте $formula$ для inline и $$formula$$ для блочных формул",
        "features": {"math": True, "codeblock": False, "table": False, "image": False, "link": True}
    },
    {
        "title": "Код и программирование",
        "placeholder": "Напишите документацию с примерами кода... Используйте ```language для блоков кода",
        "features": {"math": False, "codeblock": True, "table": False, "image": False, "link": True}
    },
    {
        "title": "Таблицы и данные",
        "placeholder": "Создайте документ с таблицами... Используйте | для создания таблиц",
        "features": {"math": False, "codeblock": False, "table": True, "image": False, "link": True}
    },
    {
        "title": "Изображения и медиа",
        "placeholder": "Добавьте изображения в ваш документ... Используйте кнопку изображения в тулбаре",
        "features": {"math": False, "codeblock": False, "table": False, "image": True, "link": True}
    },
    {
        "title": "Только текст",
        "placeholder": "Простой текстовый редактор без дополнительных функций",
        "features": {"math": False, "codeblock": False, "table": False, "image": False, "link": False}
    }
]

for example in feature_examples:
    with st.expander(example["title"]):
        st.markdown(f"**Features:** {', '.join([k for k, v in example['features'].items() if v])}")
        content = st_milkdown(
            placeholder=example["placeholder"],
            features=example["features"],
            height=200,
            key=f"context_{example['title'].replace(' ', '_')}"
        )
        if content:
            st.markdown("**Содержимое:**")
            st.code(content[:150] + "..." if len(content) > 150 else content)

# Пример с динамическим placeholder
st.subheader("5. Динамический placeholder")

placeholder_type = st.selectbox(
    "Выберите тип placeholder:",
    ["Общий", "Для заметок", "Для документации", "Для блога", "Для README", "Пользовательский"]
)

placeholder_texts = {
    "Общий": "Начните писать...",
    "Для заметок": "📝 Запишите ваши мысли и идеи здесь...",
    "Для документации": "📚 Создайте подробную документацию для вашего проекта",
    "Для блога": "✍️ Поделитесь вашими мыслями с миром...",
    "Для README": "🚀 Опишите ваш проект: что он делает, как установить и использовать",
    "Пользовательский": st.text_input("Введите свой placeholder:", "Ваш собственный placeholder...")
}

selected_placeholder = placeholder_texts[placeholder_type]

content_dynamic = st_milkdown(
    placeholder=selected_placeholder,
    height=300,
    key="dynamic_placeholder"
)

# Результаты
st.subheader("📊 Результаты")

results = {
    "basic_content": len(content_basic) if content_basic else 0,
    "ru_content": len(content_ru) if content_ru else 0,
    "en_content": len(content_en) if content_en else 0,
    "es_content": len(content_es) if content_es else 0,
    "dynamic_content": len(content_dynamic) if content_dynamic else 0,
}

st.json(results)

st.markdown("""
## 💡 Советы по использованию placeholder

1. **Будьте конкретными**: Используйте placeholder, который объясняет, что пользователь должен ввести
2. **Учитывайте контекст**: Адаптируйте placeholder под включенные features
3. **Используйте emoji**: Emoji делают placeholder более привлекательным и понятным
4. **Поддерживайте многоязычность**: Адаптируйте placeholder под язык интерфейса
5. **Не делайте слишком длинным**: Placeholder должен быть информативным, но кратким

## 🔧 API Reference

```python
st_milkdown(
    placeholder="Ваш placeholder текст здесь...",
    # другие параметры...
)
```

Параметр `placeholder` принимает строку и отображается когда редактор пустой.
""")