from gtts import gTTS
from playsound import playsound
import os

# Texto que você quer converter em áudio
texto = "Olá, este é um teste de conversão de texto em fala."

# Idioma em que você quer o áudio
idioma = 'pt'

# Passando o texto e o idioma para o gTTS
tts = gTTS(text=texto, lang=idioma, slow=False)

# Salvando o arquivo de áudio
arquivo_audio = "audio.mp3"
tts.save(arquivo_audio)

# Reproduzindo o arquivo de áudio
playsound(arquivo_audio)

# Opcional: remover o arquivo de áudio após a reprodução
os.remove(arquivo_audio)