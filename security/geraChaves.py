import rsa
import os

def gerarChaves():
    # Obtenha o caminho do diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Caminho relativo para a pasta 'keys' dentro de 'fateclando'
    keys_dir = os.path.join(script_dir, '..', 'keys')

    # Certifique-se de que a pasta 'keys' exista, criando-a se necessário
    os.makedirs(keys_dir, exist_ok=True)

    # Gero as chaves com o tamanho informado
    (pub, pri) = rsa.newkeys(2000)

    # Crio o arquivo pub
    arqnomepub = os.path.join(keys_dir, "myKeyPub.txt")
    with open(arqnomepub, 'wb') as arq:
        arq.write(pub.save_pkcs1(format='PEM'))

    # Crio o arquivo pri
    arqnomepri = os.path.join(keys_dir, "myKeyPri.txt")
    with open(arqnomepri, 'wb') as arq:
        arq.write(pri.save_pkcs1(format='PEM'))

    return arqnomepub, arqnomepri
