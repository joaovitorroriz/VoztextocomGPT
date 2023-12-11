import pyaudio
import wave

def gravar_audio(nome_arquivo, duracao, taxa_amostragem=44100, n_canais=1, largura_amostra=pyaudio.paInt16):
    """
    Grava áudio do microfone e salva em um arquivo WAV.

    :param nome_arquivo: Nome do arquivo WAV a ser criado.
    :param duracao: Duração da gravação em segundos.
    :param taxa_amostragem: Taxa de amostragem do áudio (em Hz).
    :param n_canais: Número de canais (1 para mono, 2 para estéreo).
    :param largura_amostra: Formato da amostra de áudio (pyaudio.paInt16 é comum).
    """

    p = pyaudio.PyAudio()  # Cria uma interface PyAudio

    # Abrindo stream para gravação
    stream = p.open(format=largura_amostra, channels=n_canais, rate=taxa_amostragem, input=True, frames_per_buffer=1024)

    frames = []  # Lista para armazenar os frames capturados

    print("Iniciando gravação...")

    # Lendo dados do microfone e adicionando à lista de frames
    for i in range(0, int(taxa_amostragem / 1024 * duracao)):
        data = stream.read(1024)
        frames.append(data)

    print("Gravação finalizada.")

    # Parando e fechando o stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Salvando os dados em um arquivo WAV
    with wave.open(nome_arquivo, 'wb') as wf:
        wf.setnchannels(n_canais)
        wf.setsampwidth(p.get_sample_size(largura_amostra))
        wf.setframerate(taxa_amostragem)
        wf.writeframes(b''.join(frames))

# Exemplo de uso
nome_arquivo = 'audio_gravado.wav'
duracao = 5  # Grava por 5 segundos

gravar_audio(nome_arquivo, duracao)


