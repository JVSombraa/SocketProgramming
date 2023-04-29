import socket
import random
import time
import signal
import sys

end = ('localhost', 5000)
cont = 0

def signal_end(sig, frame):
    print("Conexão finalizada.")
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_end)

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(end)

    exp = random.randint(1, 30)
    num = str(random.randint(1, (10**exp)-1))
    print("Número gerado: " + num)

    client.send(num.encode())
    print("Aguardando resposta...")

    resp = client.recv(1024).decode()
    print("Mensagem do servidor: " + resp)

    client.close()
    cont=cont+1
    print("Fim do ciclo",cont,"\n")

    for i in range(9, 0, -1):
        print(f"Loop em {i}", end="\r")
        time.sleep(1)