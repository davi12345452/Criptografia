# Algoritmo que criptografa textos usando cifra de cesar


# Usuário seta se quer encriptar ou descriptar texto
def encriptarDescriptar(texto, senha, encDesc) -> str:
    novo_texto = ""
    for letra in texto:
        if encDesc:
            nova_letra = chr(ord(letra) + senha)
        else:
            nova_letra = chr(ord(letra) - senha)
        novo_texto += nova_letra
    return novo_texto


texto = encriptarDescriptar("Ola mundo", 5, True)
print(texto)
novo_texto = encriptarDescriptar(texto, 5, False)
print(novo_texto)
