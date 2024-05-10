import random
from src.ai.ai_integration import configure_and_start_chat, send_chat_message
from utils import utils
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.layout import Layout

custom_theme = Theme({"info": "bold cyan", "user": "bold red", "ai": "bold magenta", "panel": "white"})
console = Console(theme=custom_theme)

def create_layout():
    layout = Layout()
    layout.split(
        Layout(Panel("🌿 Bem-vindo ao Peaceful Mind! 🌿", style="panel"), size=3, ratio=1),
        Layout(name="main", ratio=1),
        Layout("Digite 'fim' para encerrar a sessão", size=1)
    )
    return layout

def main():
    layout = create_layout()
    console.print(layout)
    console.print("💬 Estou aqui para te ouvir e oferecer apoio. Aguarde um momento enquanto me preparo...", style="info")
    chat = configure_and_start_chat()
    console.print("😊 Pronto! Vamos conversar? Sinta-se à vontade para compartilhar o que quiser. (Digite 'fim' para encerrar)\n", style="info")
    
    question = random.choice(utils.QUESTIONS)
    console.print(Panel(f"IA: {question}", style="ai"))

    while True:
        user_input = console.input(Panel("\nVocê: ", style="user"))
        if user_input.lower() == 'fim':
            console.print(Panel("👋 IA: Foi um prazer conversar! Até a próxima. ✨", style="ai"))
            break
        
        console.print(Panel(f"Você: {user_input}", style="user"))
        console.print(Panel("🤖 IA está digitando...", style="info"))
        response = send_chat_message(chat, user_input)
        console.print(Panel(f"IA: {response.text}", style="ai"))