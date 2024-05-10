from random import choice, randint
from src.ai.ai_integration import configure_and_start_chat, send_chat_message
from utils import utils
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.layout import Layout
from rich.progress import Progress
from rich.prompt import Prompt
from time import sleep

# Definição do tema customizado
custom_theme = Theme({"info": "bold cyan", "user": "bold red", "ai": "bold magenta", "panel": "white", "error": "bold yellow"})
console = Console(theme=custom_theme)

def main():
    console.print(Panel("                                                                                           🌿 BEM-VINDO AO PEACEFUL MIND 🌿", style="panel"))
    
    # Mensagem inicial
    console.print(Panel("💬 Estou aqui para te ouvir e oferecer apoio. Aguarde um momento enquanto me preparo...", style="info"), justify="center")
    chat = configure_and_start_chat()
    console.print(Panel("😊 Pronto! Vamos conversar? Sinta-se à vontade para compartilhar o que quiser. (Digite 'fim' para encerrar)", style="info"), justify="center")
    
    # Seleção aleatória de uma pergunta inicial
    question = choice(utils.QUESTIONS)
    console.print(Panel(f"\n{question}\n", style="ai", title="[magenta]IA[/]"))

    while True:
        user_input = Prompt.ask("\n\n[bold red]Você[/]", console=console)
        if user_input.lower() == 'fim':
            console.print(Panel("👋 IA: Foi um prazer conversar! Até a próxima. ✨", style="ai"))
            break

        with Progress(console=console, transient=True) as progress:
            task = progress.add_task("[bold cyan]🤖 IA está digitando...", total=100)
            response = send_chat_message(chat, user_input)
            while not progress.finished:
                progress.update(task, advance=randint(1, 3))
                sleep(0.1)
        console.print("\n\n")
        console.print(Panel(f"\n{response.text}\n", style="ai", title="[magenta]IA[/]"), justify="center")
