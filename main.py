from security.geraChaves import gerarChaves
from security.cifrarMsg import cifrarMsg
from security.decifrarMsg import decifrarMsg
import os

def main():
    # 1. Gerar as chaves
    print("Gerando chaves...")
    pub_key, pri_key = gerarChaves()
    print(f'Chaves geradas: \nPublic Key: {pub_key}\nPrivate Key: {pri_key}')

    # 2. Definir a mensagem de teste
    mensagem = "Esta é uma mensagem secreta"
    print(f'\nMensagem original: {mensagem}')

    # 3. Caminho para salvar a mensagem cifrada
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Corrigido: criar o caminho da pasta 'keys' corretamente
    keys_dir = os.path.join(script_dir, 'messages')
    os.makedirs(keys_dir, exist_ok=True)
    
    # Corrigido: caminho absoluto para a mensagem cifrada dentro de 'keys'
    msg_cifrada_path = os.path.join(keys_dir, 'mensagemCifrada.txt')

    # 4. Cifrar a mensagem
    print("\nCifrando mensagem...")
    cifrarMsg(pub_key, mensagem, msg_cifrada_path)

    # 5. Decifrar a mensagem
    print("\nDecifrando mensagem...")
    decifrada = decifrarMsg(pri_key, msg_cifrada_path)

    # Exibir a mensagem decifrada
    print(f'\nMensagem após decifragem: {decifrada}')

if __name__ == '__main__':
    main()
