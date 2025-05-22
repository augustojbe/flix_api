from google import genai

api_key = 'AIzaSyDpkdddpAogo5fce4JcLOfyDu0AHpfKtDk'

def get_movie_resumo(titulo, genero):
    genai.Client(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"Crie uma descrição chamativa para o filme {titulo} ({genero}), com no máximo 250 caracteres. Destaque os principais tópicos do filme."
    response = model.generate_content(prompt)
    return response.text