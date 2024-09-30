import os

##dicionario semelhante a um array de objetos
restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Pizzaria','ativo':True},
                {'nome':'Cebolao','categoria':'Marmitaria','ativo':False},
                ]

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
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)    
    print()

def opcao_invalida():
    print('Opção invalida\n')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Novo Restaurante: ')
    categoria_restaurante = input('Digite a categoria: ')
    dados_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante cadastrado com sucesso: {nome_do_restaurante}')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')
    #ljust faz ajuste de espaços em branco
    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        #capturando a chave nome
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        #if ternario
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado=True
            #alterando o booleano da chave ativo
            restaurante['ativo'] = not restaurante['ativo'] 
            #condição ternaria
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    voltar_ao_menu()

def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))    
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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