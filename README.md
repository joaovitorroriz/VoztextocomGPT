
# Assistente Virtual com Reconhecimento de Voz e Resposta Inteligente
## Descrição
Este projeto implementa um assistente virtual chamado "SARA" capaz de reconhecer voz, processar comandos de voz e responder utilizando a API da OpenAI (GPT-3.5-turbo). Ele grava áudio, converte em texto, envia para a API da OpenAI e reproduz a resposta em voz.


## Funcionalidades

- Gravação de áudio via microfone.
- Conversão de áudio para texto.
- Integração com a API da OpenAI para geração de respostas inteligentes.
- Conversão de texto para fala e reprodução de áudio.


## Pré-requisitos

- Python 3.x
- Bibliotecas Python: pyaudio, wave, threading, os, openai, gtts, playsound, speech_recognition.
- Chave de API da OpenAI.
        

## Instalação

1- Clone o repositório:
```bash
git clone https://github.com/joaovitorroriz/VoztextocomGPT.git
```
2- Navegue até o diretório do repositório clonado.

3- Instale as dependências.
```bash
pip install pyaudio wave threading os openai gtts playsound
```
    
## Configuração da Chave da API OpenAI
Antes de executar o código, você precisa configurar sua chave de API da OpenAI. Para isso:

1- Visite OpenAI e crie uma conta (se ainda não tiver uma).

2- Gere uma chave de API na sua conta OpenAI.

3- Armazene a chave de API em uma variável de ambiente. No seu terminal/bash, execute:
```bash
export OPENAI_API_KEY='sua_chave_de_api_aqui'
```

## Execução
Para executar o programa, siga estes passos:

1- Clone o repositório:
```bash
git clone https://github.com/joaovitorroriz/VoztextocomGPT.git
```
2- Navegue até o diretório do projeto:
```bash
cd VoztextocomGPT
```
3- Execute o script:
```bash
python main.py
```
## Uso

- Para gravar um áudio, pressione 'Enter' e comece a falar.
- Pressione 'Enter' novamente para terminar a gravação.
- O programa irá processar o áudio, enviar para a GPT e reproduzir a resposta.
- Digite 'sair' para encerrar o programa.
## VITS 
- Para uso do VITS clone o repositório: e adicione sua base de teste na pasta data. 

```bash
git clone https://github.com/ProgramadorArtificial/vits-portuguese.git
```



## Licença

[MIT](https://choosealicense.com/licenses/mit/)


## Autores
- [@joaovitorrorize](https://www.github.com//joaovitorroriz)

## Teste
Video do teste feito com o sistema.

[![Sistema de Conversão de Voz-Texto com GPT]()](https://youtu.be/QBWT2b3iVIA)



## Contribuições

Contribuições são sempre bem-vindas. Sinta-se à vontade para clonar, forkar ou enviar pull requests.
