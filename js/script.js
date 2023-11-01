

const startRecordingButton = document.getElementById('startRecording');
const outputText = document.getElementById('user-input');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
recognition.lang = "pt-BR"; // Define o idioma para o reconhecimento de fala (português brasileiro, por exemplo)
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

startRecordingButton.addEventListener("mousedown", () => {
    startListening();
});

startRecordingButton.addEventListener("mouseup", () => {
    stopListening();
});

function startListening() {
    startRecordingButton.style.backgroundColor = "#f7210d";
    recognition.start();

    recognition.onresult = (event) => {
        const speechToText = event.results[0][0].transcript;
        outputText.textContent = `Texto Reconhecido: ${speechToText}`;
        print("foi")
        // Enviar speechToText para o backend (por exemplo, via AJAX) para processamento com GPT.
        // Chame uma função que faz a requisição para a API do seu backend para processamento com GPT aqui.
    };
    recognition.onerror = function(event) {
        console.error("Erro de reconhecimento de fala: ", event.error);
    };

}

function stopListening() {
    startRecordingButton.style.backgroundColor = "#52ff13";
    recognition.stop(); // Para o reconhecimento de fala


    displayMessage(outputText)

}



function sendMessage() {
var userInput = document.getElementById("user-input").value;
displayMessage(userInput) 

}

function displayMessage(userInput) {   
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