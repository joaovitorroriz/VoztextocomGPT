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

def listen_for_command():
    """Função para ouvir um comando após a ativação da palavra de ativação."""
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def search_web(query):
    """Função para realizar uma pesquisa na web."""
    webbrowser.open("https://www.google.com/search?q=" + query)

def set_reminder(reminder_time, message):
    """Função para configurar um lembrete."""
    # Isso é um exemplo básico para configurar um lembrete.
    # Em uma aplicação real, você armazenaria o lembrete e verificaria o tempo continuamente.
    speak(f"Reminder set for {reminder_time}: {message}")

# Escutando pela palavra de ativação
while True:
    print("Listening for wake word...")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            if "IARA" in text:
                speak("Como posso ajudar?")
                command = listen_for_command()
                if 'search' in command:
                    query = command.replace('search', '', 1).strip()
                    search_web(query)
                elif 'reminder' in command:
                    # Extract time and message from the command
                    # This is a placeholder
                    time = '12:00'  # Example time
                    message = 'Something'  # Example message
                    set_reminder(time, message)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Service error")
