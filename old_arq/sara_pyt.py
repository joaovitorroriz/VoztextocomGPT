import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import speech_recognition as sr # pip install SpeechRecognition
from pydub import AudioSegment
import io

tokenizer = Wav2Vec2Processor.from_pretrained('jonatasgrosman/wav2vec2-large-xlsr-53-portuguese')
model = Wav2Vec2ForCTC.from_pretrained('jonatasgrosman/wav2vec2-large-xlsr-53-portuguese')

r =  sr.Recognizer()

with sr.Microphone(sample_rate=16000) as source: 
    while True:
        audio = r.listen(source) # capturar a fala AVD
        data = io.BytesIO(audio.get_wav_data())
        clip = AudioSegment.from_file(data)
        x = torch.FloatTensor(clip.get_array_of_samples()) # tensor 

        inputs = tokenizer(x,sampling_rate = 16000, return_tensor='pt',padding= 'longest').input_values
        logits = model(inputs).logits
        tokens = torch.argmax  (logits, axis = -1)
        text =  tokenizer.batch_decode(tokens)

        print("voce falou: ", str(text).lower())




        # Listar todos os microfones disponíveis e seus respectivos índices
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Índice: {}, Nome: {}".format(index, name))