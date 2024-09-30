def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "BANANA"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False    
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip() #remove os espaços na string

        index = 0 #Para exibir a posição da letra na palavra
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index +=1
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
