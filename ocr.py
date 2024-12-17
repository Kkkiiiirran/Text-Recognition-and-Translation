from PIL import Image
import pytesseract

def perform_ocr(uploaded_file, lang):
    """
    Perform OCR on an image using pytesseract.
    
    :param image_path: Path to the image file.
    :param lang: Language to use for OCR (default: "eng").
    :return: Extracted text from the image.
    """
    img = Image.open(uploaded_file)
    text = pytesseract.image_to_string(img, lang=lang)
    return text