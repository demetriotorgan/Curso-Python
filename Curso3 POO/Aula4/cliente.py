##Neste exemplo definimos uma propriedade que deixa maiscula a primeira letra
#Neste exemplo não precisamos usar os () após a função nome
##É um exemplo de getter e setter modificado. A sintaxe é como acessar a propriedade diretamente

class Cliente:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome

cliente = Cliente("marco")
print(cliente.nome)
cliente.nome = "Nico"
print(cliente.nome)