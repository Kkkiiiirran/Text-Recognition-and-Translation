# OCR + Translation with Gemini

This project extracts text from images using **pytesseract (OCR)** and translates it into a target language using **Google’s Gemini API**.  
It follows strict translation rules to ensure **exact translations** without additional text or formatting changes.  

---

## ✨ Features
- **OCR with Tesseract**  
  Extracts text from images (supports multiple languages).  

- **Gemini-powered Translation**  
  Translates extracted text from a source language to a target language with the following rules:
  1. Output only the translated text (no extra sentences).  
  2. Source and target languages must be explicitly specified.  
  3. Words/phrases in other languages remain unchanged.  
  4. Original formatting (paragraphs, bullet points) is preserved.  
  5. Translation command must follow this exact format:  
     ```
     Translate this text from {source} to {target} language.
     ```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kkkiiiirran/Text-Recognition-and-Translation

```

### 2. Create & activate a virtual environment
```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### `requirements.txt`
```
pillow
pytesseract
google-generativeai
```

### 4. Install Tesseract OCR
- **Windows:** [Download installer](https://github.com/UB-Mannheim/tesseract/wiki)  
- **Linux/macOS:**  
  ```bash
  sudo apt-get install tesseract-ocr
  ```
  or  
  ```bash
  brew install tesseract
  ```

---

## 🔑 API Key Setup
This project requires a Google Gemini API key.

1. Get your API key from [Google AI Studio](https://ai.google.dev/).  
2. Configure the key inside your script:  

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```

Alternatively, set it as an environment variable:  
```bash
export GEMINI_API_KEY="YOUR_API_KEY"   # Linux/macOS
setx GEMINI_API_KEY "YOUR_API_KEY"     # Windows
```

And update code:
```python
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## 🚀 Usage

### 1. Perform OCR on an Image
```python
from ocr_translate import perform_ocr

text = perform_ocr("scanned_doc.png", lang="eng")
print(text)
```

### 2. Start a Translation Session
```python
from ocr_translate import initialize_translation_session

chat_session = initialize_translation_session()
```

### 3. Translate Extracted Text
```python
from ocr_translate import translate_text

translated = translate_text(chat_session, text, source_lang="Hindi", target_lang="English")
print(translated)
```

---

## 📝 Example Workflow

```python
# Step 1: OCR
ocr_text = perform_ocr("document.jpg", lang="hin")  
print("Extracted Text:\n", ocr_text)

# Step 2: Initialize translation session
chat = initialize_translation_session()

# Step 3: Translate
translation = translate_text(chat, ocr_text, source_lang="Hindi", target_lang="English")
print("\nTranslated Text:\n", translation)
```

---

## ⚠️ Translation Rules
- No additional explanations.  
- Only the translated text should be returned.  
- Numbers should also be translated.  
- Formatting (paragraphs, bullet points) should be preserved.  

---

## 📂 Project Structure
```
ocr-gemini-translate/
│── ocr_translate.py       # Core OCR + translation functions
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

---

## ✅ Future Enhancements
- Add **Streamlit UI** for uploading images and viewing translations.  
- Support **batch translations**.  
- Cache translations to reduce API calls.  

---

## 🤝 Contributing
Pull requests are welcome! Please fork the repo and open a PR with improvements.  

---

## 📜 License
MIT License © 2025  
