from flask import Flask, request
import speech_recognition as sr
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                with open("transcription.txt", "w") as file:
                    file.write(text)
                return "Transcrição salva: " + text
            except sr.UnknownValueError:
                return "Áudio não entendido"
            except sr.RequestError as e:
                return f"Erro de serviço: {e}"
    return "Nenhum áudio recebido"

if __name__ == '__main__':
    app.run(debug=True)
