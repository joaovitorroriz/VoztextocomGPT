import whisper
import speech_recognition as sr 
model = whisper.load_model('base')

r = sr.Recognizer()

with sr.Microphone() as mic:
    while True:  
        print('Diga algo:')
        audio = r.listen(mic)

        with open('temp.wav', 'wb') as f:
            f.write(audio.get_wav_data())

        result =  model.transcribe('temp.wav')
        print('voce', result['text'])