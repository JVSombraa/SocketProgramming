import socket
import random
import string
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

end = ('localhost', 5000)

server.bind(end)
server.listen(1)

while True:
    print("Aguardando conexão...")
  
    client, end_client = server.accept()
    print("Conexão realizada com " + str(end_client))

    num = client.recv(1024).decode()
    print("Mensagem recebida: " + num)

    if len(num) < 10:
        if int(num) % 2 == 0:
            resp = "PAR"
        else:
            resp = "IMPAR"
    else:
        resp = ''.join([random.choice(string.ascii_letters) for i in range(len(str(num)))])

    client.send(resp.encode())
    print("Mensagem enviada: " + resp)

    client.close()

    print("Fim da conexão.\n")
    time.sleep(1)