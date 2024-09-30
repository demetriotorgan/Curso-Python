class Conta:
    def __init__(self, numero, titulo, saldo, limite):
        #print(f"Contruindo objeto...{self}")
        self.numero = numero
        self.titulo = titulo
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titulo}")
    
    def deposita(self, valor):
        self.saldo += valor
        print(f"Valor depositado {valor}")
        print(f"Novo saldo: {self.saldo}")
    
    def saca(self, valor):
        self.saldo -= valor
        print(f"Valor sacado: {valor}")
        print(f"Novo saldo: {self.saldo}")

#Instanciando um nova conta
conta = Conta(123,"Nico", 55.5,1000.0)
conta.extrato()
conta.deposita(100)
conta.saca(30)
