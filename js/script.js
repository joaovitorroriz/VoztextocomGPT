
let audioChunks = [];
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
        // Evita o comportamento padrão de "Enter" (enviar formulário)
        event.preventDefault();
        // Mantém o foco no campo de entrada após pressionar "Enter"
        userInput.focus();
        // Chama a função para enviar a mensagem (ou outra lógica, se desejado)
        enviarMensagem();
        console.log(data);

    }
});


navigator.mediaDevices.getUserMedia({ audio: true })
  .then(function (stream) {
    const mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = function (event) {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = function () {
      const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
      const formData = new FormData();
      formData.append('audio', audioBlob,'audio.wav');

      fetch('/upload', {
        method: 'POST',
        body: formData
      })
        .then(response => response.json())
        .then(data => {
          // Faça algo com a resposta do servidor, se necessário
          console.log(data);
        })
        .catch(error => {
          console.error('Erro ao enviar áudio para o servidor:', error);
        });

      audioChunks = [];
    };

    startRecordingButton.addEventListener("mousedown", () => {
    startRecordingButton.style.backgroundColor = "#f7210d";
    mediaRecorder.start();
    });

    startRecordingButton.addEventListener("mouseup", () => {
    startRecordingButton.style.backgroundColor = "#52ff13";
    mediaRecorder.stop();
    });
  })
  .catch(function (err) {
    console.error('Erro ao acessar o dispositivo de áudio:', err);
  });




// startRecordingButton.addEventListener("mousedown", () => {
//     startListening();
// });
// startRecordingButton.addEventListener("mouseup", () => {
//     stopListening();
// });
// function startListening() {
//     startRecordingButton.style.backgroundColor = "#f7210d";
//     recognition.onresult = (event) => {
//         const speechToText = event.results[0][0].transcript;
//         var textospeech = ` ${speechToText}`;
//         // Enviar speechToText para o backend (por exemplo, via AJAX) para processamento com GPT.
//         // Chame uma função que faz a requisição para a API do seu backend para processamento com GPT aqui.
//     };
//     recognition.onerror = function(event) {
//         console.error("Erro de reconhecimento de fala: ", event.error);
//     };
//     recognition.start();   
//     // displayMessage(textospeech)
// }
// function stopListening() {
//     startRecordingButton.style.backgroundColor = "#52ff13";
//     recognition.stop(); // Para o reconhecimento de fala
//     displayMessage(textospeech)
// }



function sendMessage(message) {
displayMessage(message) 

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

function enviarMensagem() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        // Se o campo de entrada não estiver vazio, envie a mensagem
        displayMessage(userInput);
        // Limpe o campo de entrada após enviar a mensagem (opcional)
        document.getElementById("user-input").value = "";
    } else {
        // Se o campo de entrada estiver vazio, você pode exibir uma mensagem de erro ou fazer outra ação
        console.log("Por favor, digite uma mensagem antes de enviar.");
    }
}