from prettyconf import config


class Settings:
    API_KEY = config("API_KEY", default="")
    
    
    SAFETY_SETTINGS = {
        'HATE': 'BLOCK_NONE',
        'HARASSMENT': 'BLOCK_NONE',
        'SEXUAL' : 'BLOCK_NONE',
        'DANGEROUS' : 'BLOCK_NONE'
    }
    GENERATION_CONFIG = {
        "candidate_count": 1,
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 5,
    }
    SYSTEM_INSTRUCTION = (
    "Atuar como um terapeuta virtual avançado, oferecendo suporte emocional e "
    "conselhos baseados em terapia cognitivo-comportamental, com ênfase em práticas "
    "de relaxamento e mindfulness. O modelo deve ser empático, informativo e cauteloso, "
    "encorajando os usuários a buscar ajuda profissional quando necessário. BE HUMAN!"
    )

settings = Settings()
