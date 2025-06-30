from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
plaintext = "SECRETS MESSAGE"
ciphertext = cipher.encrypt(pad(plaintext).encode())
print("AES :", base64.b64encode(ciphertext).decode())
