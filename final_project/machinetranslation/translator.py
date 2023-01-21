"""
This module handles translation from english to french and vice versa
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-07-11',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    This function translates english text to french text
    """
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation


def french_to_english(french_text):
    """
    This function translate french text to english text
    """
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation
