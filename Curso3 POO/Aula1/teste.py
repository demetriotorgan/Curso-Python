##Modelo procedural de conta
#Existem vários problemas com esse modelo
#Pois os dados e criação de novas contas estão fracamente relacionadas

def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite        
    }
    return conta

def depositars(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f"Saldo atual: {conta["saldo"]}")

