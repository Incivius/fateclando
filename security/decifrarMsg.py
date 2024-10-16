import rsa

def decifrarMsg(arqnomepri, arqnomemsg):
    with open(arqnomepri, 'rb') as arq:
        pri_key_data = arq.read()

    # Decodifico para o formato expoente e modulo
    pri = rsa.PrivateKey.load_pkcs1(pri_key_data, format='PEM')

    # Abro o arquivo com a msg cifrada
    with open(arqnomemsg, 'rb') as arq:
        msgc = arq.read()

    # Decifro a msg
    msg = rsa.decrypt(msgc, pri).decode('utf-8')

    print(f'Mensagem decifrada: {msg}')
    return msg
