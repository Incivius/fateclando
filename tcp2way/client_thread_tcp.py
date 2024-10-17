#Cliente TCP
import socket
import os
from dotenv import load_dotenv
from threading import Thread
from security.decifrarMsg import decifrarMsg
from security.cifrarMsg import cifrarMsg

def client(pri, pub):
    global tcp_con
    
    def receber():
        global tcp_con
        while True:
            msg = tcp_con.recv(1050)
            msg = decifrarMsg(pri, msg)
            print ("Server:", msg)

    def enviar():
        global tcp_con
        print('Para sair use CTRL+X\n')
        msg = input()
        msg = cifrarMsg(pub, msg)
        print(f'Mensagem: {msg}')
        while msg != '\x18':
            # Remova o .encode(), já que msg já está em formato de bytes
            tcp_con.send(msg)
            msg = input()
            msg = cifrarMsg(pub, msg)  # Cifrar a nova mensagem antes de enviar
        tcp_con.close()

    # Endereco IP do Servidor
    SERVER = '192.168.56.1'
    # Porta que o Servidor esta escutando
    PORT = 5003

    tcp_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (SERVER, PORT)
    tcp_con.connect(dest)


    t_rec = Thread(target=receber, args=())
    t_rec.start()

    t_env = Thread(target=enviar, args=())
    t_env.start()