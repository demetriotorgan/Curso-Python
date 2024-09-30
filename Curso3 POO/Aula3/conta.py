#Getters e Setter em python

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
    
    ##Getter que retornam algum valor dos atributos
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titulo
    
    def get_limite(self):
        return self.__limite
    
    #Altera o limite do titular
    def set_limite(self,limite):
        self.__limite = limite


#Instanciando um nova conta
conta1 = Conta(123,"Nico", 50.0,1000.0)
conta2 = Conta(321,"Marco", 100,2000.0)

print(conta1.get_saldo())
print(conta1.get_titular())
print(conta1.get_limite())

conta1.set_limite(2000)
print(conta1.get_limite())
