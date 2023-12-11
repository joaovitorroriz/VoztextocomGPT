import speech_recognition as sr

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Gravar áudio do microfone
with sr.Microphone() as source:
    print("Fale algo...")
    audio = recognizer.listen(source)

    try:
        # Usar o reconhecedor para converter o áudio em texto
        text = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: " + text)

        # Salvar o texto em um arquivo
        with open("transcricao.txt", "w") as file:
            file.write(text)

    except sr.UnknownValueError:
        print("Não entendi o áudio")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados; {e}")
