import random
from src.ai.ai_integration import configure_and_start_chat, send_chat_message
from utils import utils
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"info": "bold cyan", "user": "bold red", "ai": "bold magenta"})
console = Console(theme=custom_theme)

def main():
    console.print("🌿 Bem-vindo ao Espaço de Escuta! 🌿\n", style="info")
    console.print("💬 Estou aqui para te ouvir e oferecer apoio. Aguarde um momento enquanto me preparo...", style="info")
    chat = configure_and_start_chat()
    console.print("😊 Pronto! Vamos conversar? Sinta-se à vontade para compartilhar o que quiser. (Digite 'fim' para encerrar)\n", style="info")
    
    question = random.choice(utils.QUESTIONS)
    console.print(f"\nIA: {question}", style="ai")

    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() == 'fim':
            console.print("👋 IA: Foi um prazer conversar! Até a próxima. ✨", style="ai")
            break

        console.print("\n🤖 IA está digitando...\n", style="info")
        response = send_chat_message(chat, user_input)
        console.print(f"\nIA: {response.text}\n", style="ai")