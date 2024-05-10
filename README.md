# 🌿 Peaceful Mind 🌿 Um Chatbot de Apoio Emocional com TCC e Mindfulness

## Descrição
Este projeto apresenta um chatbot de suporte emocional construído com o modelo de linguagem Gemini, do Google Generative AI. O chatbot utiliza princípios da Terapia Cognitivo-Comportamental (TCC) e práticas de relaxamento e mindfulness para oferecer apoio e orientação a usuários que estejam passando por momentos de estresse, ansiedade ou depressão.

## Funcionalidades
- **Conversas Empáticas e Informativas**: O chatbot foi desenvolvido para oferecer uma experiência de conversa natural e empática, fornecendo informações relevantes sobre saúde mental e bem-estar.
- **Práticas de TCC**: Auxilia os usuários a identificar pensamentos disfuncionais, trabalhar com o Registro de Pensamentos Disfuncionais (RPD) e aplicar técnicas de descatastrofização.
- **Técnicas de Relaxamento e Mindfulness**: Guia os usuários em exercícios de respiração, relaxamento muscular progressivo e visualização.
- **Orientação para Ajuda Profissional**: Encoraja os usuários a buscar ajuda especializada quando necessário.
- **Integração de Artigos Científicos**: Treinado com uma base de grandes artigos científicos da área da psicologia sobre TCC e mindfulness, garantindo a qualidade e a confiabilidade das informações fornecidas.

## Tecnologias Utilizadas
- **Google Generative AI (Gemini)**: Modelo de linguagem avançado utilizado para o processamento de linguagem natual e gerar respostas coerentes e, contextualmente relevantes.
- **Python**: Linguagem de programação utilizada para o desenvolvimento do chatbot e integração com a API do Google Generative AI.
- **Rich**: Biblioteca para formatação e estilização de texto na interface do chatbot.
- **Prettyconf**: Biblioteca para gerenciamento de configurações do projeto.

## Como Utilizar
1. Clone o repositório do projeto (usando HTTPS ou exporte em um ZIP).
2. Instale as dependências listadas no arquivo `requirements.txt`.


```bash
pip install -r .\requirements.txt
```


3. Configure a sua chave de API do Google Generative AI:
    3.1.  Transforme o arquivo `local.env` em `.env`;
    3.2.  Insira sua chave no local indicado -> "your_api_key" (mantendo as chaves duplas);
   
5. Execute o arquivo `run.py` para iniciar o chatbot.


```bash
python .\run.py 
```


6. Converse com o chatbot e explore as funcionalidades oferecidas. 😊

## Observações
- Este chatbot é um protótipo e não substitui o acompanhamento profissional de um psicólogo ou psiquiatra.
- O chatbot está em constante desenvolvimento e novas funcionalidades serão adicionadas no futuro.

## Recursos Adicionais
- [Mindfulness-Based Cognitive Therapy](https://www.umassmed.edu/cfm/](https://www.psychologytoday.com/intl/therapy-types/mindfulness-based-cognitive-therapy))
- [University of Massachusetts Medical School, Center for Mindfulness](https://www.umassmed.edu/cfm/](https://www.umassmed.edu/psychiatry/education/mindfulphysicianleadershipprogram/general-mindfulness/))

Espero que este chatbot possa ser um recurso valioso para promover a saúde mental e o bem-estar!
