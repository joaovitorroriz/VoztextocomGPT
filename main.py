import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# iniciando text to speech
engine = pyttsx3.init('espeak')  # Para windons #pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# func to speek text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# func to recognize speech

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio,language ='pt-br')
        print(f"usuario disse: {query}\n")

    except Exception as e:
        print("Poderia dizer novamente...")
        return "None"
    
    return query

# func crar lista
def create_todo_list():
    speak("O que voce quer adicionar a sua lista de tarefas?")
    task = recognize_speech()
    with open('todo.txt','a') as f:
        f.write(f"{datetime.datetime.now()} -{task}\n")
    speak("tarefa adicionada")


# func pesquisar web 
def search_web():
    speak("O que voce gostaria de procurar?")
    query = recognize_speech()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Aqui esta os resultados para {query}.")


# func reminder
def set_reminder():
    speak("o que eu devo lembra-lo?")
    task = recognize_speech()
    speak("Emquantos minutos ")
    mins =  recognize_speech()
    mins = int(mins)
    reminder_time = datetime.datetime.now() +datetime.timedelta(minutes=mins)
    with open ('reminders.txt','a') as f:
        f.write(f"{reminder_time} - {task}\n")
    speak(f"Lembrete definido para {mins} minutos a partir de agora.  ")




#main func para rodar o assistant 
def main():
    speak("Ola, Eu sou assistente pessoal. Em que posso ajudar?")
    while True:
        query = recognize_speech().lower()

        if 'criar uma lista de tarefas' in query:
            create_todo_list()
        elif 'procurar na web' in query:
            search_web()
        elif 'criar um lembrete' in query:
            set_reminder()

        elif "pare" in query or "sair" in query:
            speak("Ate logo!")
            break
        else:
            speak("Desculpe, Nao entendi, Poderia repetir?")

main()
