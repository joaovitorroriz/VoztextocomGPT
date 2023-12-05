from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Adiciona suporte a CORS para todos os endpoints



@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']

    audio_file.save('audio.wav')

    # Faça o que quiser com o arquivo de áudio, por exemplo, salvá-lo no servidor
    # audio_file.save('caminho/do/seu/arquivo/audio.wav')
    return 'Áudio recebido com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
