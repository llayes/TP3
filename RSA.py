import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Générer les clés
key = RSA.generate(2048)
public_key = key.publickey()
cipher_rsa = PKCS1_OAEP.new(public_key)

message = b"SECRETS MESSAGE"
cipher_rsa_text = cipher_rsa.encrypt(message)
print("RSA :", base64.b64encode(cipher_rsa_text).decode())
