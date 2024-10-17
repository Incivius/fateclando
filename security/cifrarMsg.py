import rsa

def cifrarMsg(arqnomepub, msg, arqnomemsg):
    with open(arqnomepub, 'rb') as arq:
        pub_key_data = arq.read()

    # Decodifico para o formato expoente e modulo
    pub = rsa.PublicKey.load_pkcs1(pub_key_data, format='PEM')

    # Cifro a msg
    msgc = rsa.encrypt(msg.encode('utf-8'), pub)

    # Salvo a msg cifrada no arquivo
    with open(arqnomemsg, 'wb') as arq:
        arq.write(msgc)

    print(f'Mensagem cifrada salva no arquivo: {arqnomemsg}')
    return msgc
