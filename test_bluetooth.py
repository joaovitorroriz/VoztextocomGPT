import bluetooth
import time

# Substitua pelo endereço MAC do seu fone de ouvido Bluetooth
target_address = "00:00:00:00:00:00"

# Criar um socket Bluetooth
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Conectar ao dispositivo
sock.connect((target_address, 1))

# Enviar um sinal e medir o tempo de resposta
try:
    while True:
        start_time = time.time()
        sock.send("ping")
        data = sock.recv(1024)
        end_time = time.time()
        
        if data == "pong":
            rtt = end_time - start_time
            # Converta o RTT em distância aqui (muito impreciso para Bluetooth)
            print(f"RTT: {rtt} segundos")

        time.sleep(1)

except KeyboardInterrupt:
    sock.close()
