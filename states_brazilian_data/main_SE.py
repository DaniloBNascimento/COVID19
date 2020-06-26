import os
import csv
import time
# URL_base = https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/7f5ff801706b28fbdb4be818043c37a4_Download_COVID19_20200428.csv
# Função de limpar a tela:
def cleanup():
    os.system('clear')
    #end
print("Zerando cache de dados anteriores...")
time.sleep(2)
os.system('rm -rf db.csv')
time.sleep(2)
cleanup()
print("Aguarde o download do banco de dados...")
time.sleep(2)
os.system('wget https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/7f5ff801706b28fbdb4be818043c37a4_Download_COVID19_20200428.csv')
os.system('mv  7f5ff801706b28fbdb4be818043c37a4_Download_COVID19_20200428.csv db.csv')
cleanup()
print("Download realizado com sucesso!")
time.sleep(2)
cleanup()
print("Realizando a leitura dos dados coletados...")
time.sleep(2)
with open('db.csv', 'r') as arquivo_csv:
    lendo = csv.reader(arquivo_csv, delimiter=',')
    for coluna in lendo:
        print(coluna)

