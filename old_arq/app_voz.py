import speech_recognition as sr
import openai

# Configuração da chave de API da OpenAI
openai.api_key = 'sua_chave_de_api_da_openai'

# Função para converter voz para texto usando SpeechRecognitiondeactivate
def voz_para_texto():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
        return None
    except sr.RequestError as e:
        print("Erro na solicitação ao Google Speech Recognition service; {0}".format(e))
        return None

# Função para interagir com GPT-3.5 da OpenAI
def interagir_com_gpt(texto):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=texto,
        max_tokens=150  # Defina o número máximo de tokens na resposta
    )
    return resposta.choices[0].text.strip()

# Função principal
def main():
    while True:
        entrada_de_voz = voz_para_texto()
        if entrada_de_voz:
            resposta_do_gpt = interagir_com_gpt(entrada_de_voz)
            print("Resposta do GPT: " + resposta_do_gpt)

if __name__ == "__main__":
    main()
