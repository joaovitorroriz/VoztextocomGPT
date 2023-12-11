
import whisper
import speech_recognition as sr

from pydub import AudioSegment
audio = AudioSegment.from_mp3("w01.mp3")
audio.export("w01.wav", format="wav")


model = whisper.load_model("base")
result = model.transcribe("w01.mp3")
print(result["text"])


print("###########/n")

import speech_recognition as sr
r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Fale algo:")
#     audio = r.listen(source)
with sr.AudioFile('w01.wav') as source:
    audio = r.record(source)

try:
    print("Texto Reconhecido: " + r.recognize_google(audio, language="pt-BR"))
except sr.UnknownValueError:
    print("Google Web Speech não conseguiu entender o áudio")
except sr.RequestError as e:
    print("Não foi possível obter resultados do serviço Google Web Speech; {0}".format(e))

