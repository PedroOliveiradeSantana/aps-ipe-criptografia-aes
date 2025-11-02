
# Sistema de criptografia AES para comunicação segura em áreas contaminadas
# Simulação de envio e recepção de mensagem confidencial

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Geração da chave simétrica e vetor de inicialização (IV)
chave = get_random_bytes(16)  # 128 bit
iv = get_random_bytes(16)

# Entrada da mensagem a ser criptografada
mensagem = input("Mensagem confidencial: ")
mensagem_bytes = mensagem.encode('utf-8')

# Preenchimento da mensagem com padding
mensagem_preenchida = pad(mensagem_bytes, AES.block_size)

# Criação do objeto de cifragem
cifrador = AES.new(chave, AES.MODE_CBC, iv)
mensagem_cifrada = cifrador.encrypt(mensagem_preenchida)

# Codificação da mensagem e do IV para Base64
mensagem_b64 = base64.b64encode(mensagem_cifrada).decode('utf-8')
iv_b64 = base64.b64encode(iv).decode('utf-8')

# Exibição dos dados criptografados
print("\nMensagem criptografada (Base64):")
print(mensagem_b64)

print("\nIV utilizado (Base64):")
print(iv_b64)

# Simulação de decodificação
mensagem_recebida = base64.b64decode(mensagem_b64)
iv_recebido = base64.b64decode(iv_b64)

# Criação do objeto de decifragem
decifrador = AES.new(chave, AES.MODE_CBC, iv_recebido)
mensagem_decifrada = decifrador.decrypt(mensagem_recebida)

try:
    mensagem_original = unpad(mensagem_decifrada, AES.block_size)
    print("\nMensagem decifrada com sucesso:")
    print(mensagem_original.decode('utf-8'))
except ValueError:
    print("\nErro ao remover padding. A mensagem pode ter sido corrompida.")
