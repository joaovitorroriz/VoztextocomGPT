import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Inicializa o reconhecedor e o motor de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Função para falar o texto."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Função para ouvir e reconhecer a fala."""
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            return text
        except sr.UnknownValueError:
            return "Não entendi"
        except sr.RequestError:
            return "Erro de serviço"

def search_web(query):
    """Função para realizar pesquisa na web."""
    webbrowser.open("https://www.google.com/search?q=" + query)

def set_reminder(reminder_time, message):
    """Função para configurar um lembrete."""
    current_time = datetime.datetime.now()
    target_time = datetime.datetime.strptime(reminder_time, '%H:%M')
    while current_time < target_time:
        current_time = datetime.datetime.now()
    speak(f"Lembrete: {message}")

# Loop principal
while True:
    speak("Como posso ajudar?")
    query = listen()
    if 'pesquisa' in query:
        search_query = query.replace('pesquisa', '')
        search_web(search_query)
    elif 'lembrete' in query:
        # Extrai o horário e a mensagem da consulta
        # Isso é um exemplo, necessita de um processamento mais sofisticado
        time = '12:00'  # Horário de exemplo
        message = 'Almoçar'  # Mensagem de exemplo
        set_reminder(time, message)
    elif 'sair' in query:
        break
