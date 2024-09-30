import os

def exibir_nome_programa():
    print("""      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    print('1.Cadastrar restaurante')
    print('2.Listar Restaurante')
    print('3.Ativar Restaurante')
    print('4.Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o App\n')

def escolher_opcao():
    ##Salvando o valor digitado em um inteiro
    opcao_escolhida = int(input('Escolha uma opção: '))

    ##Exibindo informações
    ##print('Opção escolhida: ', opcao_escolhida)
    ##print(f'Opção escolhida: {opcao_escolhida}')

    ##Tipo das variáveis
    #print(type(opcao_escolhida))
    #print(type(1))


    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

##Definindo uma funcao main
def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()