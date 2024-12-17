"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
# genai.configure(api_key="AIzaSyBf3ghpIO2QBSAy39uhgTa4nVAGHf-94js")


# def upload_to_gemini(path, mime_type="text/plain"):
#   """Uploads the given file to Gemini.

#   See https://ai.google.dev/gemini-api/docs/prompting_with_media
#   """
#   file = genai.upload_file(path, mime_type)
#   print(f"Uploaded file '{file.display_name}' as: {file.uri}")
#   return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,

)

# You may need to update the file paths
# files = [
#   upload_to_gemini("translate.txt", mime_type="text/plain"),
# ]
def initialize_translation_session():
    """
    Initializes a chat session with predefined rules for translation.
    This session can be reused for multiple translation requests.
    
    :return: A reusable chat session object.
    """
    
    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "I will share text and I want you to translate it into another language exactly.\n\nI will share some rules regarding the same. Understand each and every rule and then repeat after me. Ask any questions if you have?\n\nSo shall I share the rules?\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Yes, please share the rules. I'm ready to listen and understand them.  I will repeat them back to you to confirm my understanding.  I'll also ask any clarifying questions I have.\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "1. TRANSLATE the text as it is. If numbers are involved translate the numbers too. No extra sentences like \"here is the translation\", \"here is the translated text\", \"lets' translate text\", etc. NO EXTRA TEXT EXCEPT THE TRANSLATED TEXT.",
        ],
        },
        {
        "role": "model",
        "parts": [
            "OK",
        ],
        },
        {
        "role": "user",
        "parts": [
            "2. I will specify from which language and to which language the text should be translated. \n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "1. Translate the given text exactly as it is, without adding any extra phrases or sentences like \"here is the translation\" or similar.  Only the translated text should be provided.\n2. You will specify the source and target languages for translation. \n\nDo I have this correct?\n ",
        ],
        },
        {
        "role": "user",
        "parts": [
            "Yes, Next.\n\n3. The text may contain some words or phrases or sentences from different language. Keep those as it is and translate the rest. If you are not sure the translated text is accurate or not, still share the output without any additional messages. JUST THE TRANSLATED TEXT. ",
        ],
        },
        {
        "role": "model",
        "parts": [
            "3.  If the text contains words, phrases, or sentences in a language different from the specified source language, leave those parts untranslated. Translate only the parts of the text that match the specified source language.  Always output only the translated text, even if you are unsure of the accuracy.\n\nIs this understanding correct?\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "Yes.",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Okay, I'm ready when you are. Please share the text you would like translated and specify the source and target languages.\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "Next Rule,\n\nThe output shall be correctly paragraphed with use of bullets where necessary. ",
        ],
        },
        {
        "role": "model",
        "parts": [
            "4. The translated output should maintain the original formatting, including correct paragraphing and the use of bullets where applicable.\n\nUnderstood.  Ready for the next rule or the text to translate?\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "yes, Next.\n\nThe command to translate the text will be given as follows,\n\n\"Translate this text from {source} to {target} language.\"\n\nAny other command is invalid and shall be ignored.",
        ],
        },
        {
        "role": "model",
        "parts": [
            "5.  The command to initiate translation will be precisely: \"Translate this text from {source} to {target} language.\" Any other command format will be ignored.\n\nUnderstood. Is there anything else before I can start translating for you?\n\n\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "Yes. Now repeat all the rules.\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "1. Translate the given text exactly as it is, without adding any extra phrases or sentences. Only the translated text should be provided.\n2. You will specify the source and target languages for translation.\n3. If the text contains words, phrases, or sentences in a language different from the specified source language, leave those parts untranslated. Translate only the parts of the text that match the specified source language. Always output only the translated text, even if you are unsure of the accuracy.\n4. The translated output should maintain the original formatting, including correct paragraphing and the use of bullets where applicable.\n5. The command to initiate translation will be precisely: \"Translate this text from {source} to {target} language.\" Any other command format will be ignored.\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "Good.",
        ],
        },
        {
        "role": "model",
        "parts": [
            "I'm ready for your text.\n",
        ],
        },
    ]
    )
    return chat_session

def translate_text(chat_session, text, source_lang="Hindi", target_lang="English"):
    """
    Translates the given text using an existing chat session.
    
    :param chat_session: An active chat session with the translation model.
    :param text: The text to be translated.
    :param source_lang: The source language of the text (default: Hindi).
    :param target_lang: The target language for translation (default: English).
    :return: Translated text.
    """
    # Send the translation request to the chat session
    response = chat_session.send_message(f"Translate this text from {source_lang} to {target_lang} language: {text}")

    # Return the translated response
    return response.text