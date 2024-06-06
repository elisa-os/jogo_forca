import palavras
import boneco
import val_try_show_word as vtsw


def jogar_forca():
    palavra = palavras.escolher_palavra()
    letras_corretas = set()
    tentativas = 7
    
    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra:")
    print(vtsw.mostrar_palavra(palavra, letras_corretas))
    
    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()
        
        if not vtsw.validar_tentativa(letra):
            continue
        
        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
        elif letra in palavra:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
            boneco.exibir_forca(tentativas)
        
        print(vtsw.mostrar_palavra(palavra, letras_corretas))
        
        if '#' not in vtsw.mostrar_palavra(palavra, letras_corretas):
            print("Parabéns! Você venceu!")
            return
        
    print("Você perdeu! A palavra era:", palavra)


# Executar o jogo
jogar_forca()
