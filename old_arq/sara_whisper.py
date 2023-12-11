
import os
import openai
from gtts import gTTS
from playsound import playsound
import whisper

# Initialize the API key

idioma = 'pt'
openai.api_key = os.getenv('OPENAI_API_KEY')

def gerar_resposta(messages):
    #response = openai.ChatCompletion.create( ## Api antiga
    response = openai.chat.completions.create( ## API nova
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]

mensagens = [{"role": "system", "content": "Você é um assistente gente boa, seu nome é SARA"}]

while True:
    # Ask a question
    question = input("Perguntar para Sara (\"sair\"): ")

    if question == "sair" or question == "":
        print("saindo")
        break
    else:
        mensagens.append({"role": "user", "content": str(question)})

        answer = gerar_resposta(mensagens)
        print("user:", question)
        print("Sara:", answer[0], "\nCusto:\n", answer[1])
        mensagens.append({"role": "assistant", "content": answer[0]})
        tts = gTTS(text=answer[0], lang=idioma, slow=False)
        
        # Salvando o arquivo de áudio
        arquivo_audio = "audio.mp3"
        tts.save(arquivo_audio)

        # Reproduzindo o arquivo de áudio google
        playsound(arquivo_audio)

        # Opcional: remover o arquivo de áudio após a reprodução
        os.remove(arquivo_audio)

        
    debugar = False
    if debugar:
        print("Mensagens", mensagens, type(mensagens))