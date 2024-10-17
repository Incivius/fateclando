import rsa

def decifrarMsg(arqnomepri, msgc):
    # Carregar a chave privada a partir do arquivo
    with open(arqnomepri, 'rb') as arq:
        pri_key_data = arq.read()

    # Decodificar a chave privada
    pri = rsa.PrivateKey.load_pkcs1(pri_key_data, format='PEM')

    # Decifrar a mensagem cifrada recebida (em formato de bytes)
    msg = rsa.decrypt(msgc, pri).decode('utf-8')

    print(f'Mensagem decifrada: {msg}')
    return msg