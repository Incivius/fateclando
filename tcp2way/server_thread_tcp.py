#Servidor TCP
import os
from dotenv import load_dotenv
import socket
from threading import Thread
from security.cifrarMsg import cifrarMsg

global tcp_con

def enviar():
    global tcp_con
    msg = input()
    while True:
        msg = cifrarMsg(
            arqnomepub='keys/myKeyPub.txt',
            msg=msg,
            arqnomemsg='messages/mensagemCifrada.txt'
        )
        tcp_con.send(msg)
        msg = input()

# Endereco IP do Servidor
HOST = os.getenv('HOST')

# Porta que o Servidor vai escutar
PORT = 5003

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msg = tcp_con.recv(1024)
        if not msg: break
        print("Cliente:",msg)
    print ('Finalizando conexao do cliente', cliente)
    tcp_con.close()
