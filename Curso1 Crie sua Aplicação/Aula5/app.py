import os

restaurantes = ['Pizza','Sushi']

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
    exibir_subtitulo('Finalizando App...')

def voltar_ao_menu():
    input('Digite uma tecla para retornar ao menu... ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Novo Restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante cadastrado com sucesso: {nome_do_restaurante}')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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