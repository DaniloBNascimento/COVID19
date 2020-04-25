# Descrição: Script criado para consumir dados de uma API sobre o corona vírus.
# Autor: Danilo Bastos Nascimento
# Data de criação: 25/04/2020
# ----------------------------------------------
# Importando módulos necessários
import json
import requests

# Definindo variáveis
url = requests.get('https://api.covid19api.com/summary')
content = json.loads(url.content)
validate = url.status_code
count = -1
# Validando conexão com o servidor de dados (API)
if validate != 200:
    print("Servidor de dados indisponível ou falha na conexão!")
    print("ERROR status code: "+str(validate))

# Main execução:
print("Estado atual da conexão: "+str(validate))
# chave e valor JSON
#print(content.keys())
print(" ")
while count != 246:
    count = count + 1
    num_pais = content['Countries'][count]
    num_cases = num_pais['TotalConfirmed']
    pais = content['Countries'][count]['Country']
    deaths = content['Countries'][count]['NewDeaths']
    try:
        percent_deaths = (deaths / num_cases) * 100
    except ZeroDivisionError:
        percent_deaths = 0
    print("País/Região: "+str(pais))
    print("Número de casos total: " +str(num_pais['TotalConfirmed']))
    print("Número de mortes: "+str(deaths))
    str_percents_deaths = str(percent_deaths)
    print("Índice de mortalidade de acordo com número de casos: "+str_percents_deaths[0:4]+"%")
    print("")
