
#        Ambiente virtual
# Instalar o virtualenv (se ainda não estiver instalado):
    pip install virtualenv
# Criar um novo ambiente virtual:
    virtualenv venv
# Ativar o ambiente virtual:
    source venv/bin/activate   OU  deactivate

# Instale as dependências usando o requirements.txt:
    pip install -r requirements.txt
# Atualize o requirements.txt
    pip freeze > requirements.txt

# Instalar o Flask:
    pip install flask
    pip install flask-cors

# Lista todas as branches no repositório.
    git branch
# Descarta as alterações não salvas em seus arquivos.
    git restore: 
# Envia as alterações do branch local para o branch main no repositório remoto no GitHub.
    git push origin main 
# Cria e muda para uma nova branch chamada ubuntu2.
    git checkout -b ubuntu2:
# Mostra o status das alterações na nova branch ubuntu2. 
    git status
# Adiciona todas as alterações no diretório de trabalho ao índice para o próximo commit.
    git add .
# Confirma as alterações adicionadas ao índice com uma mensagem de commit específica.   
    git commit -m "Adicionar arquivo ubuntu2"
# Envia as alterações do branch local para o repositório remoto na branch atual.
    git push

# SpeechRecognition
pip install SpeechRecognition openai
Empurrar Mudanças para o Repositório Remoto:

  git push origin main.


cadastre uma chave de acesso no site da openai 
openai.api_key = os.getenv('OPENAI_API_KEY')


google 
pip install gtts
pip install playsound