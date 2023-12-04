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
