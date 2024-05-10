def extract_pdf_pages(pathname: str) -> list[str]:
    parts = [f"--- START OF PDF ${pathname} ---"]
    # Add logic to read the PDF and return a list of pages here.
    pages = []
    for index, page in enumerate(pages):
        parts.append(f"--- PAGE {index} ---")
        parts.append(page)
    return parts

class Utils:
    QUESTIONS = [
        "Você tem sentido que as coisas que antes te davam prazer perderam o sentido? Conte-me um pouco sobre como você tem se sentido em relação às suas atividades diárias.",
        "Você tem se sentido triste ou desanimado ultimamente? Pode me descrever como tem sido seu estado de espírito em geral?",
        "Como tem sido seu sono recentemente? Você tem tido dificuldade para dormir, ou tem dormido mais do que o normal?",
        "Você tem se sentido cansado ou com falta de energia? Como isso tem afetado suas atividades diárias?",
        "Você notou alguma mudança em seu apetite recentemente? Tem comido mais ou menos do que o habitual?",
        "Como você tem se sentido em relação a si mesmo ultimamente? Você tem se sentido culpado ou desapontado consigo mesmo?",
        "Você tem tido dificuldade para se concentrar ou prestar atenção nas coisas? Pode me dar alguns exemplos?",
        "Você tem notado alguma mudança na sua velocidade de movimento ou fala? Ou talvez você tenha se sentido mais inquieto ou agitado do que o normal?",
        "Você tem tido pensamentos sobre morte ou sobre se machucar? É importante que você saiba que pode falar sobre isso comigo, e eu estou aqui para te ajudar.",
    ]   
    HISTORY = [
    {
    "role": "user",
    "parts": extract_pdf_pages("src\\articles\\mindfulness_2.pdf")
    },
    {
    "role": "user",
    "parts": extract_pdf_pages("src\\articles\\mindfulness.pdf")
    },
    {
    "role": "user",
    "parts": extract_pdf_pages("src\\articles\\tcc_1.pdf")
    },
    {
    "role": "user",
    "parts": extract_pdf_pages("src\\articles\\tcc_2.pdf")
    },
]
    
utils = Utils()