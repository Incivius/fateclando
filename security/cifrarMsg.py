import rsa

def cifrarMsg(arqnomepub, msg):
    try:
        # Abrir e ler a chave pública do arquivo
        with open(arqnomepub, 'rb') as arq:
            pub_key_data = arq.read()

        # Decodificar para o formato de chave pública
        pub = rsa.PublicKey.load_pkcs1(pub_key_data, format='PEM')

        # Cifrar a mensagem
        msgc = rsa.encrypt(msg.encode('utf-8'), pub)

        print(f'Mensagem: {msgc}')

        # Retornar a mensagem cifrada
        return msgc
    except Exception as e:
        print(f"Erro ao cifrar a mensagem: {e}")
        return None
