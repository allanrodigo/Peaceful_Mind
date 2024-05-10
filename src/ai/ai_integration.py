import google.generativeai as genai
from config.settings import settings
from utils import utils


def configure_and_start_chat():
    genai.configure(api_key=settings.API_KEY)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        generation_config=settings.GENERATION_CONFIG,
        safety_settings=settings.SAFETY_SETTINGS,
        system_instruction=settings.SYSTEM_INSTRUCTION
    )
    chat = model.start_chat(history=utils.HISTORY)
    return chat

def send_chat_message(chat, message):
    return chat.send_message(message)
