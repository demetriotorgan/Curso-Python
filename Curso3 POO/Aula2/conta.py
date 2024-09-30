##OBS: Em Python quando usamos dois underline __ estamos dizedno que aquele atributo é privado da classe
##Neste caso dizemos que os atributos foram encapsulados a classe
##Importante: Os valores dos atributos encapsulados só podem ser alterados via algum método não pode ser modificado diretamente

class Conta:
    def __init__(self, numero, titulo, saldo, limite):
        print(f"Contruindo objeto...{self}")
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titulo}")
    
    def deposita(self, valor):
        self.__saldo += valor
        print(f"Valor depositado {valor}")
        print(f"Novo saldo: {self.__saldo}")
    
    def saca(self, valor):
        self.__saldo -= valor
        print(f"Valor sacado: {valor}")
        print(f"Novo saldo: {self.__saldo}")
    
    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)


#Instanciando um nova conta
conta1 = Conta(123,"Nico", 50.0,1000.0)
conta2 = Conta(321,"Marco", 100,2000.0)

conta2.transfere(100,conta1)
conta2.extrato()
conta1.extrato()

