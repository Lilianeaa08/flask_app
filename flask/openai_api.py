import requests
import os
import dotenv
dotenv.load_dotenv("/home/liliane/DOCKER/docker_file/config/.env")

CHAVE_API = os.getenv("CHAVE_API")

api_key = CHAVE_API

# Endpoint da API de Chat da OpenAI
url = 'https://api.openai.com/v1/chat/completions'

def analise_openai(texto: str) -> str:
    try:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Você é um especialista em turismo e o seu principal papel é recomendar as pessoas de forma resumida, para onde elas podem viajar com os melhores preços e custo benefício, você indicará sempre três sugestões."},
                {"role": "user", "content": texto}
            
            ],
            "temperature": 0.8,
            "max_tokens": 230,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

        response = requests.post(url, json=data, headers=headers)

        return response.json()['choices'][0]['message']['content']
    
    except requests.exceptions.RequestException as e:
        return "API indisponível" 