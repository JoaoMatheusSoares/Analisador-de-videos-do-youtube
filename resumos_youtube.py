import openai
import requests
from pytube import YouTube
import os

# Configure sua chave de API da OpenAI
openai.api_key = 'sua-chave-api'

def baixar_video_youtube(url):
    """Baixa o áudio de um vídeo do YouTube e extrai a transcrição"""
    try:
        yt = YouTube(url)
        print(f"Baixando áudio de: {yt.title}")

        # Selecionando o stream de áudio de melhor qualidade
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        
        if not stream:
            print("Erro: Não foi possível encontrar stream de áudio.")
            return None
        
        # Baixando o arquivo de áudio
        audio_file = stream.download(filename="audio.mp4")
        print(f"Áudio baixado com sucesso: {audio_file}")
        return audio_file

    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return None

def gerar_resumo(texto):
    """Gera o resumo do texto usando OpenAI GPT"""
    try:
        print("Gerando resumo...")
        prompt = f"Resuma o seguinte texto:\n\n{texto}"
        response = openai.Completion.create(
            model="text-davinci-003",  # Ou use o modelo GPT-4 se preferir
            prompt=prompt,
            max_tokens=200,  # Número máximo de tokens para o resumo
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Erro ao gerar resumo: {e}")
        return None

def main(url):
    """Função principal que identifica o tipo de URL e gera um resumo"""
    if 'youtube.com' in url:
        # Caso a URL seja de um vídeo do YouTube
        print("Detectado YouTube, baixando áudio...")
        audio_file = baixar_video_youtube(url)
        if not audio_file:
            return "Erro ao baixar o vídeo."

        # Aqui você deve adicionar a transcrição do áudio usando um serviço de transcrição
        # Exemplo fictício de transcrição:
        transcricao = "Aqui deveria estar a transcrição do áudio."
        resumo = gerar_resumo(transcricao)
        return resumo
    else:
        return "URL não suportada."

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    resultado = main(url)
    print("Resumo gerado:\n")
    print(resultado)
