import sys
import os
import streamlit as st
from ocr import perform_ocr
from translate import initialize_translation_session, translate_text
from PIL import Image
from google import genai

# -----------------------------------
# ✅ Configure Google API
# -----------------------------------

from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# -----------------------------------
# ✅ Point Tesseract to your custom tessdata directory
# -----------------------------------
# Example path — update it if your folder name or location differs
os.environ["TESSDATA_PREFIX"] = os.path.join(os.getcwd(), "tessdata")

# Optionally verify:
print("TESSDATA_PREFIX set to:", os.environ["TESSDATA_PREFIX"])

# -----------------------------------
# ✅ Main Streamlit app
# -----------------------------------
def main():
    st.title("OCR and Translation App")
    
    # Upload image(s)
    uploaded_files = st.file_uploader(
        "Upload Images", 
        type=["png", "jpg", "jpeg", "bmp", "gif"], 
        accept_multiple_files=True
    )

    # Language selections
    source_lang = st.selectbox("Select Source Language", 
                               ["English", "Hindi", "Gujarati", "Bengali", "French", "Spanish"])
    target_lang = st.selectbox("Select Target Language", 
                               ["English", "Hindi", "Gujarati", "Bengali", "French", "Spanish"])
    
    # Initialize translation
    chat_session = initialize_translation_session()

    if st.button("Translate"):
        if uploaded_files:
            translated_texts = []

            # Language map for Tesseract codes
            lang_map = {
                "English": "eng",
                "Hindi": "hin",
                "Gujarati": "guj",
                # "Punjabi": "pun",
                "Bengali": "ben",
                "Spanish": "spa",
                "French": "fra"
            }

            lang = lang_map.get(source_lang, "eng")

            for uploaded_file in uploaded_files:
                img = Image.open(uploaded_file)
                st.image(img, caption=f"Uploaded Image - {uploaded_file.name}", width=300)

                # Perform OCR
                extracted_text = perform_ocr(uploaded_file, lang)
                st.write(f"**Extracted Text from {uploaded_file.name}:**\n{extracted_text}")

                # Translate
                translated_text = translate_text(chat_session, extracted_text, source_lang, target_lang)
                translated_texts.append((uploaded_file.name, translated_text))
                st.write(f"**Translated Text for {uploaded_file.name}:**\n{translated_text}")

            # Download button for results
            if translated_texts:
                result = "\n\n".join([f"{fname}:\n{txt}" for fname, txt in translated_texts])
                st.download_button("Download Translations", result, "translated_texts.txt", "text/plain")
        else:
            st.error("Please upload at least one image.")

# Run the app
if __name__ == "__main__":
    main()
