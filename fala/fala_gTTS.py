from gtts import gTTS
from pydub import AudioSegment
import simpleaudio as sa

import os

while True:
    # Obter texto do usuário
    text = input("Digite um texto (ou 'sair' para finalizar): ")
    if text.lower() in ['sair', 'parar', 'finalizar']:
        break

    # Usar gTTS para sintetizar o texto
    tts = gTTS(text, lang='pt-br')

    # Salvar o áudio sintetizado em um arquivo MP3
    mp3_file = "temp_audio.mp3"
    tts.save(mp3_file)

    # Converter MP3 para WAV
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = "temp_audio.wav"
    audio.export(wav_file, format="wav")

    # Reproduzir o arquivo WAV
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Esperar até a reprodução terminar

    # Limpar arquivos temporários
    os.remove(mp3_file)
    os.remove(wav_file)

print("Programa encerrado.")
