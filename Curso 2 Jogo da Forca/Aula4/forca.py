import random

def jogar():    
    imprime_abertura()    
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
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


def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")    
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    #print(palavras)
    numeroAleatorio = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numeroAleatorio]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()