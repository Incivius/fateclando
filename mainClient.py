from security.geraChaves import gerarChaves
from security.cifrarMsg import cifrarMsg
from security.decifrarMsg import decifrarMsg
from tcp2way.client_thread_tcp import client
import os

def main():
    # 1. Gerar as chaves
    print("Gerando chaves...")
    pub_key, pri_key = gerarChaves()
    print(f'Chaves geradas: \nPublic Key: {pub_key}\nPrivate Key: {pri_key}')

    client()
    
if __name__ == '__main__':
    main()
