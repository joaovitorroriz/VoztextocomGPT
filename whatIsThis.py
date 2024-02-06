import pyaudio
import wave
import threading
import os
import openai
from gtts import gTTS
from playsound import playsound
from openai import OpenAI
import speech_recognition as sr



class Chatbot:
    def __init__(self):
        self.question_types = [0, 0, 0, 0, 0]  # [what, who, where, when, why]
        self.question_names = ["what", "who", "where", "when", "why"]  # [what, who, where, when, why]

    def analyze_question(self, user_input):
        user_input = user_input.lower()
        if 'sair' in user_input:
            print("Saindo do chatbot...")
            return False
        if 'what' in user_input:
            self.question_types[0] = 1
            self.what()
        if 'who' in user_input:
            self.question_types[1] = 1
            self.who()
        if 'where' in user_input:
            self.question_types[2] = 1
            self.where()
        if 'when' in user_input:
            self.question_types[3] = 1
            self.when()
        if 'why' in user_input:
            self.question_types[4] = 1
            self.why()
        
        return True

    def what(self):
        print("Método 'what' chamado.")     #   O que    explicação 

    def who(self):
        print("Método 'who' chamado.")      #   Quem       individuo 

    def where(self):
        print("Método 'where' chamado.")    #   Onde        localidade

    def when(self):
        print("Método 'when' chamado.")     #   Quando      tempo 

    def why(self):
        print("Método 'why' chamado.")      #   Por que    motivo

    def salvar_svg(self, array_strings, nome_arquivo):
        # Construir o conteúdo SVG
        conteudo_svg = "<svg width='200' height='100'>\n"
        for string in array_strings:
            conteudo_svg += f"  {string}\n"
        conteudo_svg += "</svg>"

        # Escrever o conteúdo SVG em um arquivo
        with open(nome_arquivo, "w") as arquivo_svg:
            arquivo_svg.write(conteudo_svg)

        print(f"O arquivo {nome_arquivo} foi salvo com sucesso.")


# Exemplo de uso:
chatbot = Chatbot()
while True:
    user_input = input("Digite sua pergunta (ou 'sair' para sair): ")
    if not chatbot.analyze_question(user_input):
        break
