def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "BANANA"    
    enforcou = False
    acertou = False
    

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip() #remove os espaços na string

        index = 0 #Para exibir a posição da letra na palavra
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f'A letra {letra} está na posição: {index}')                
            index +=1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
