def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result

# Exemple
chiffre_affine = affine_encrypt("SECRETS", a=5, b=8)
print("Affine :", chiffre_affine)
