import math

def calcul_entropie(texte):
    freq = {}
    for caractere in texte:
        freq[caractere] = freq.get(caractere, 0) + 1
    total = len(texte)
    entropie = -sum((f / total) * math.log2(f / total) for f in freq.values())
    return entropie

def calcul_redondance(texte):
    alphabet_size = 26  # supposons texte en lettres uniquement
    return 1 - (calcul_entropie(texte) / math.log2(alphabet_size))

def indice_coincidence(texte):
    N = len(texte)
    freq = {}
    for c in texte:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    somme = sum(f * (f - 1) for f in freq.values())
    return somme / (N * (N - 1)) if N > 1 else 0

if __name__ == "__main__":
    texte = "HELLOHELLO"
    print("Entropie du texte :", calcul_entropie(texte))
    print("Redondance du texte :", calcul_redondance(texte))
    print("Indice de coïncidence :", indice_coincidence(texte))
