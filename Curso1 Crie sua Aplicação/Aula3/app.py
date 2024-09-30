import os

restaurantes = []

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

def opcao_invalida():
    print('Opção invalida\n')
    input('Digite novamente')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrando um novo Restaurante')
    nome_do_restaurante = input('Novo Restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante cadastrado com sucesso: {nome_do_restaurante}')
    input('Digite uma tecla para voltar ao menu principal...')
    main()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


##Definindo uma funcao main
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()