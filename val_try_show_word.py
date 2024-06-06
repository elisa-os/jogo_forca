def validar_tentativa(chute):
    if len(chute) != 1:
        print("Por favor, digite apenas uma letra.")
        return False
    elif not chute.isalpha():
        print("Por favor, digite apenas letras.")
        return False
    else:
        return True
    
def mostrar_palavra(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += '#'
    return resultado
