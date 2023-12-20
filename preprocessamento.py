from preprocessamento.preparando_base import converter_mp4_para_wav
from preprocessamento.tratar_audio import dividir_audios
from preprocessamento.tratar_legenda import criar_csv

# converte audio.mp4 para audio.wav
# converter_mp4_para_wav()
# print("Conversão concluída")

# Chamar a função de processamento
# dividir_audios()
# print("Divisão concluída")

# Atualiza o aquivo texts com a descrição 
criar_csv()
print("Atualização concluída")