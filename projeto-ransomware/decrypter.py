import os
import pyaes

# Solicita o caminho do arquivo

file_name = input("Digite o caminho do arquivo a ser descriptografado ").strip()

file_name = file_name + ".cryptOFF"
if not os.path.exists(file_name):
    print("Erro: O arquivo específico não foi encontrado")
else:
    try:
        # Abrir e ler o arquivo
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Chave de descriptografia com 32 bytes
        key = b"testeransomwares_security_crypt!"

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Cria um nome de arquivo removendo a extensão ".cryptOFF"
        decrypted_file_name = file_name.replace(".cryptOFF", "")

        # Salvando o arquivo descriptografado
        with open(decrypted_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
