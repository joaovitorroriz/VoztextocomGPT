document.getElementById('start-record-btn').addEventListener('click', function() {
    // Iniciar gravação
    this.disabled = true;
    document.getElementById('stop-record-btn').disabled = false;
    document.getElementById('recording-instructions').innerText = 'Gravação iniciada. Fale no microfone.';
    let mediaRecorder;
    let audioChunks = [];
    
    // Solicitar acesso ao microfone
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };
        })
        .catch(error => console.error("Erro ao obter acesso ao microfone:", error));});

document.getElementById('stop-record-btn').addEventListener('click', function() {
    // Parar gravação
    this.disabled = true;
    document.getElementById('start-record-btn').disabled = false;
    document.getElementById('recording-instructions').innerText = 'Gravação parada. Você pode ouvir o áudio ou gravar novamente.';
    // Aqui você adicionaria o código para parar a gravação e processar o áudio
});


// Função para iniciar a gravação
function startRecording() {
    if (mediaRecorder) {
        audioChunks = [];
        mediaRecorder.start();
        console.log("Gravação iniciada...");
    }
}

// Função para parar a gravação
function stopRecording() {
    if (mediaRecorder) {
        mediaRecorder.stop();
        console.log("Gravação parada.");
        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/mpeg-3' });
            const audioUrl = URL.createObjectURL(audioBlob);
            const audio = new Audio(audioUrl);
            audio.play();
        };
    }
}

// Adicionando event listeners aos botões
document.getElementById('start-record-btn').addEventListener('click', startRecording);
document.getElementById('stop-record-btn').addEventListener('click', stopRecording);
