import torch._classes
import streamlit as st
from PIL import Image
import os
from models.blip_loader import load_blip_model, generate_caption
from utils.caption_formatter import instagram_format, generate_hashtags, translate_caption

st.set_page_config(page_title="Image Caption Generator", layout="centered")
st.title("📸 AI Image Caption Generator")

model, processor = load_blip_model()

uploaded_files = st.file_uploader("Drag and drop images here", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        caption = generate_caption(model, processor, image)
        st.subheader("📝 Caption")
        st.success(caption)

        st.subheader("📱 Instagram-Ready Caption")
        st.info(instagram_format(caption))

        st.subheader("🏷️ Hashtag Suggestions")
        st.code(generate_hashtags(caption))

        st.subheader("🌍 Translated Captions")
        for lang_code, lang_name in [("hi", "Hindi"), ("es", "Spanish"), ("fr", "French")]:
            translated = translate_caption(caption, lang_code)
            st.write(f"**{lang_name}:** {translated}")
