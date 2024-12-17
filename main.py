import sys
# print(sys.version)
import os
import streamlit as st
from ocr import perform_ocr
from translate import initialize_translation_session, translate_text
from PIL import Image
# from dotenv import load_dotenv
import os
from dotenv import load_dotenv
import google.generativeai as genai
import sys
# print(sys.version)

# Load environment variables from .env file
# load_dotenv()

# Fetch the API key from the environment variables
api_key = os.getenv("api_key")

if api_key is None:
    raise ValueError("API Key is missing. Please check your .env file.")

# Configure the Google AI API with the API key
genai.configure(api_key=api_key)

# Rest of your code remains the same...


def main():
    st.title("OCR and Translation App")
    
    # Upload image folder
    uploaded_files = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg", "bmp", "gif"], accept_multiple_files=True)

    # Select source and target languages
    source_lang = st.selectbox("Select Source Language", ["English", "Hindi", "Punjabi", "Gujarati", "Bengali", "French", "Spanish"])
    target_lang = st.selectbox("Select Target Language", ["English", "Hindi", "Punjabi", "Gujarati", "Bengali", "French", "Spanish"])
    
    # Initialize translation session
    chat_session = initialize_translation_session()

    if st.button("Translate"):
        if uploaded_files:
            translated_texts = []
            
            for uploaded_file in uploaded_files:
                # Perform OCR on the uploaded image
                img = Image.open(uploaded_file)
                st.image(img, caption=f"Uploaded Image - {uploaded_file.name}", width=300)
                if source_lang == "English":
                    lang = "eng"
                elif source_lang == "Hindi":
                    lang="hin"
                elif source_lang == "Gujarati":
                    lang="guj"
                elif source_lang == "Punjabi":
                    lang="pun"
                elif source_lang=="Bengali":
                    lang="ben"
                elif source_lang=="Spanish":
                    lang="spa"
                elif source_lang =="French":
                    lang="fra"

                extracted_text = perform_ocr(uploaded_file, lang)
                st.write(f"**Extracted Text from {uploaded_file.name}:**\n{extracted_text}")

                # Translate the extracted text
                translated_text = translate_text(chat_session, extracted_text, source_lang, target_lang)
                translated_texts.append((uploaded_file.name, translated_text))
                st.write(f"**Translated Text for {uploaded_file.name}:**\n{translated_text}")

            # Optionally, provide a download link for the results
            if translated_texts:
                result = "\n\n".join([f"{image_file}:\n{translated_text}" for image_file, translated_text in translated_texts])
                st.download_button("Download Translations", result, "translated_texts.txt", "text/plain")
        else:
            st.error("Please upload at least one image.")

# def configure():
#     load_dotenv()
if __name__ == "__main__":
    # configure()
    main()

