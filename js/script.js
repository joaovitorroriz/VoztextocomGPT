

const startRecordingButton = document.getElementById('startRecording');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = 'pt-BR';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

// Obtém o elemento de entrada do usuário
var userInput = document.getElementById("user-input");

// Adiciona um evento de tecla pressionada ao elemento de entrada do usuário
userInput.addEventListener("keyup", function(event) {
    // Verifica se a tecla pressionada é a tecla "Enter"
    if (event.key === 'Enter') {
        // Chama a função sendMessage() quando a tecla "Enter" é pressionada
        sendMessage();
    }
});

startRecordingButton.addEventListener('click', () => {
    recognition.start();

    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;
        outputText.textContent = `Texto Reconhecido: ${speechToText}`;

        // Enviar speechToText para o backend (por exemplo, via AJAX) para processamento com GPT.
        // Chame uma função que faz a requisição para a API do seu backend para processamento com GPT aqui.
    };

    recognition.onerror = (event) => {
        console.error('Erro de Reconhecimento de Fala:', event.error);
    };
});





function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatHistory = document.getElementById("chat-history");
    
    // Adicione a mensagem do usuário ao histórico de conversas
    chatHistory.innerHTML += "<p><strong>Você:</strong> " + userInput + "</p>";
    
    // Lógica do chatbot - substitua esta parte com a lógica do seu chatbot real
    var botResponse = "Olá! Eu sou um chatbot.";
    
    // Adicione a resposta do chatbot ao histórico de conversas
    chatHistory.innerHTML += "<p><strong>Chatbot:</strong> " + botResponse + "</p>";
    
    // Limpe o campo de entrada do usuário
    document.getElementById("user-input").value = "";
    
    // Role para o final do histórico de conversas
    chatHistory.scrollTop = chatHistory.scrollHeight;
}
