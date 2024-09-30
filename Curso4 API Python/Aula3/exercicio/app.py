#Configurando o ambiente
# python -m venv venv
# Ativando o ambiente virtual, entrar na pasta Scripts e
# activate.bat

#Para desativar
# deactivate

#-------Importanto o Request
# pip install requests

# Para verificar: pip freeze

#Criando o txt requirements:  pip freeze > requirements.txt

import requests
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    cotacao = float(data['USDBRL']['bid'])
    mensagem = f"U$ 1 dólar corresponde a R$ {cotacao:.2f}"
    print(mensagem)
else:
    print(f"A requisição falhou: {response.status_code}")
