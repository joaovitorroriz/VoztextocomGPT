const startRecordingButton = document.getElementById('startRecording');
const userInput = document.getElementById('user-input');
const chatHistory = document.getElementById('chat-history');

function startListening() {
    startRecordingButton.style.backgroundColor = "#f7210d";

    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;
        textospeech = ` ${speechToText}`;
        // Enviar speechToText para o backend (por exemplo, via AJAX) para processamento com GPT.
        // Chame uma função que faz a requisição para a API do seu backend para processamento com GPT aqui.
    };
    recognition.onerror = function(event) {
        console.error("Erro de reconhecimento de fala: ", event.error);
    };
    recognition.start(); displayMessage(textospeech);
}

function stopListening() {
    startRecordingButton.style.backgroundColor = "#52ff13";
    recognition.stop(); // Para o reconhecimento de fala
    displayMessage(textospeech);
}

function displayMessage(message) {
    const userMessage = document.createElement('p');
    userMessage.textContent = `Você: ${message}`;
    chatHistory.appendChild(userMessage);

    // Lógica do chatbot - substitua esta parte com a lógica do seu chatbot real
    const botResponse = 'Olá! Eu sou um chatbot.';
    const botMessage = document.createElement('p');
    botMessage.textContent = `Chatbot: ${botResponse}`;
    chatHistory.appendChild(botMessage);

    // Role para o final do histórico de conversas
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function enviarMensagem() {
    const message = userInput.value.trim();
    if (message !== '') {
        // Se o campo de entrada não estiver vazio, envie a mensagem
        displayMessage(message);
        // Limpe o campo de entrada após enviar a mensagem (opcional)
        userInput.value = '';
    } else {
        // Se o campo de entrada estiver vazio, você pode exibir uma mensagem de erro ou fazer outra ação
        console.log('Por favor, digite uma mensagem antes de enviar.');
    }
}

startRecordingButton.addEventListener('mousedown', () => {
    startListening();
});

startRecordingButton.addEventListener('mouseup', () => {
    stopListening();
});

userInput.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault();
        userInput.focus();
        enviarMensagem();
    }
});
