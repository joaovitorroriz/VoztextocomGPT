import speech_recognition as sr
import pyaudio
# miclist=sr.Microphone.list_microphone_names()
# print(miclist)
# print("########/n")


# Listar todos os dispositivos de microfone
# pa = pyaudio.PyAudio()
# for index in range(pa.get_device_count()):
#     desc = pa.get_device_info_by_index(index)
#     print(f"Dispositivo {index}: {desc['name']}")
# print("########/n")

def record_and_save_audio(audio):
    with open("saved_audio.wav", "wb") as file:
        file.write(audio.get_wav_data())

def save_transcript(text):
    with open("transcript.txt", "w") as file:
        file.write(text)

def main():
    recognizer = sr.Recognizer()    
    microphone = sr.Microphone() # 11 default      device_index=mic_index

    # recognizer.energy_threshold = 1568 
    # recognizer.dynamic_energy_threshold = True

    print("Ouvindo...")

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            # recognizer.energy_threshold = 1932
            # recognizer.dynamic_energy_threshold = True
            # recognizer.pause_threshold=1.2
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(text)

            if text.startswith("Sara pesquisar"):
                command_text = text[len("Sara pesquisar "):]
                record_and_save_audio(audio)
                save_transcript(command_text)
                print("Comando salvo e transcrito.")
            else:
                 print(command_text)    #  print

        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError:
            print("Erro de serviço; verifique sua conexão com a internet.")

if __name__ == "__main__":
    main()
