#!/usr/bin/env python3
"""
Quick test script to verify the min_height parameter works correctly
"""

import streamlit as st
from streamlit_crepe import st_milkdown

st.title("Min Height Parameter Test")

st.subheader("Default min_height (400px)")
content1 = st_milkdown(
    default_value="# Small content",
    key="editor1"
)

st.subheader("Custom min_height (200px)")
content2 = st_milkdown(
    default_value="# Small content",
    min_height=200,
    key="editor2"
)

st.subheader("Custom min_height (600px)")
content3 = st_milkdown(
    default_value="# Small content",
    min_height=600,
    key="editor3"
)

st.subheader("Fixed height (overrides min_height)")
content4 = st_milkdown(
    default_value="# Small content",
    height=300,
    min_height=600,  # This should be ignored
    key="editor4"
)

st.write("**Results:**")
st.write(f"Editor 1: {len(content1)} chars")
st.write(f"Editor 2: {len(content2)} chars")
st.write(f"Editor 3: {len(content3)} chars")
st.write(f"Editor 4: {len(content4)} chars")