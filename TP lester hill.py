import numpy as np

def hill_encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")
    while len(message) % len(key_matrix) != 0:
        message += 'X'

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""

    for i in range(0, len(message), len(key_matrix)):
        block = [letters.index(c) for c in message[i:i+len(key_matrix)]]
        block = np.dot(key_matrix, block) % 26
        encrypted += ''.join([letters[int(num)] for num in block])
    
    return encrypted

# Exemple
key = np.array([[3, 3], [2, 5]])
message = "SECRETS"
chiffre = hill_encrypt(message, key)
print("Hill :", chiffre)