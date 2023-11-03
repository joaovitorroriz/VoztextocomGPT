const fs = require('fs');
const record = require('node-record-lpcm16');
const wav = require('wav');

const file = fs.createWriteStream('output.wav', { encoding: 'binary' });
const reader = new wav.Reader();

reader.on('format', function (format) {
  // Inicializa o gravador com o formato do arquivo de áudio
  const recorder = record.record({
    sampleRate: format.sampleRate,
    channels: format.channels,
    audioType: format.audioType,
  });

  // Captura o áudio do microfone
  recorder.pipe(file);
});

// Inicia a gravação
record.start().pipe(reader);
console.log('Gravando...');

// Pressione qualquer tecla para parar a gravação
process.stdin.setRawMode(true);
process.stdin.resume();
process.stdin.on('data', function() {
  console.log('Parando a gravação...');
  record.stop();
  process.exit();
});
