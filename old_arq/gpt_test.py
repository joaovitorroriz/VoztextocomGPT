import speech_recognition as sr

def ouvir_microfone():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            texto = rec.recognize_google(audio, language='pt-BR')
            return texto
        except sr.UnknownValueError:
            return "Não entendi"

texto_ouvido = ouvir_microfone()


from gtts import gTTS

def texto_para_fala(texto, nome_arquivo):
    tts = gTTS(texto, lang='pt-br')
    tts.save(nome_arquivo)

# Exemplo de uso
texto_para_fala("Olá, mundo!", "ola_mundo.mp3")