import pyaudio
import wave
import audioop

# Definição dos parâmetros de áudio
FORMAT = pyaudio.paInt16  # Formato dos dados de áudio (int16)
CHANNELS = 1              # Mono (1 canal)
RATE = 44100              # Taxa de amostragem
CHUNK = 1024              # Tamanho do bloco de gravação
WAVE_OUTPUT_FILENAME = "output.wav"  # Nome do arquivo de saída

# Inicialização do PyAudio
audio = pyaudio.PyAudio()

# Abertura do stream de gravação
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Gravando... (fale agora)")

frames = []
silent_chunks = 0
silence_limit = 20  # Aproximadamente 2 segundos de silêncio para terminar a gravação

# Função para verificar se o áudio está abaixo do limiar de silêncio
def is_silent(data_chunk, threshold=500):
    """ Retorna 'True' se abaixo do 'threshold' de 'silent' """
    return max(audioop.rms(data_chunk, 2), 0) < threshold

# Loop de gravação
while True:
    data = stream.read(CHUNK)
    frames.append(data)

    # Verifica se o áudio é silencioso
    if is_silent(data):
        silent_chunks += 1
        if silent_chunks > silence_limit:
            print("Silêncio detectado, gravação finalizada.")
            break
    else:
        silent_chunks = 0

# Parando e fechando o stream
stream.stop_stream()
stream.close()
audio.terminate()

# Salvando o arquivo WAV
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
