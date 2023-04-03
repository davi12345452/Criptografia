# Algortimo que simula a cifra de Vigenere

# Temos de usar a tabela de Vigenere para entender melhor o funcionamento dessa cifra
# Mas basicamente ocorre um deslocamento para cada letra e esse deslocamento é feito
# pela key. É uma Cifra de Cesar mais complexa

def encrypt_vigenere(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    key_index = 0
    for letter in message:
        if letter in alphabet:
            shift = alphabet.index(key[key_index])
            letter_index = alphabet.index(letter)
            encrypted += alphabet[(letter_index + shift) % 52]
            key_index = (key_index + 1) % len(key)
        else:
            encrypted += letter
    return encrypted


def decrypt_vigenere(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    key_index = 0
    for letter in message:
        if letter in alphabet:
            shift = alphabet.index(key[key_index])
            letter_index = alphabet.index(letter)
            decrypted += alphabet[(letter_index - shift) % 52]
            key_index = (key_index + 1) % len(key)
        else:
            decrypted += letter
    return decrypted

# Fácil de descriptografar, as palavras ficam com mesmo tamanho

print(encrypt_vigenere("Estou lhe transmitindo uma mensagem", "feiufgwei"))
print(decrypt_vigenere("jWbiZ RdI bWEVmROpMVIS cgF SaRaFKMg", "feiufgwei"))