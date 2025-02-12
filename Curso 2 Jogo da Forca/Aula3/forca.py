def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "BANANA".upper()
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False    
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() #remove os espaços na string

        if(chute in palavra_secreta):
            index = 0 #Para exibir a posição da letra na palavra
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index +=1
        else:
            erros +=1
        enforcou = erros ==6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns voce acertou!!!")
    else:
        print("Tente novamente")

if(__name__ == "__main__"):
    jogar()
