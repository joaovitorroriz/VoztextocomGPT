
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