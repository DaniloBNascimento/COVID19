# Descrição: Script criado para consumir dados de uma API sobre o corona vírus.
# Autor: Danilo Bastos Nascimento
# Data de criação: 25/04/2020
# ----------------------------------------------
# Importando módulos necessários
import json
import requests
import time
import os
print("Aguardando estabelecer conexão...")
# Definindo variáveis
# Validando conexão com o servidor de dados (API)
try:
    url = requests.get('https://api.covid19api.com/summary')
except:
    print("Servidor de dados indisponível ou falha na conexão!")
    exit(0)
content = json.loads(url.content)
count = -1
validate = url.status_code
# Main execução:
print("Estado atual da conexão: "+str(validate))
time.sleep(3)
os.system('clear')
# chave e valor JSON
#print(content.keys())
print(" ")
print("Status global:")
# variaveis de status global
world_total_cases = content['Global']['TotalConfirmed']
world_total_mortes = content['Global']['TotalDeaths']
str_world_total_cases = str(content['Global']['TotalConfirmed'])
str_world_total_mortes = str(content['Global']['TotalDeaths'])
try:
    world_percent_deaths = (world_total_mortes / world_total_cases) * 100
except ZeroDivisionError:
    world_percent_deaths = 0
str_world_percent_deaths = str(world_percent_deaths)
print("Total de casos: "+str_world_total_cases[0]+","+str_world_total_cases[1:3]+"milhões")
print("Total de mortes: "+str_world_total_mortes[0:3]+"mil")
print("Letalidade Mundial: "+str_world_percent_deaths[0:4]+"%")
print("-------------------------------------------------")
time.sleep(10)
print("Relatorio por pais/regiao:")
while count != 245:
    count = count + 1
    num_pais = content['Countries'][count]
    num_cases = num_pais['TotalConfirmed']
    pais = content['Countries'][count]['Country']
    deaths = content['Countries'][count]['TotalDeaths']
    try:
        percent_deaths = (deaths / num_cases) * 100
    except ZeroDivisionError:
        percent_deaths = 0
    print("País/Região: "+str(pais))
    print("Número de casos total: " +str(num_pais['TotalConfirmed']))
    print("Número de mortes: "+str(deaths))
    str_percents_deaths = str(percent_deaths)
    print("Letalidade: "+str_percents_deaths[0:4]+"%")
    print("")
    time.sleep(1)
