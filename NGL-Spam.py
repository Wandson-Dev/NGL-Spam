import requests
import os
import time
import sys

f = '\033[m'
vermelho = '\033[31m'
v = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'

def ngl():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{amarelo}Projeto by {f}{ciano}@wandson.dev 🤠\n{f}')
    time.sleep(2)
    
    if len(sys.argv) > 1:
        nglusername = sys.argv[1]
    else:
        nglusername = input(f'{azul}Digite o Nome de Usuário Para o Spammer: {f}')
    mensagem = input(f'{azul}Mensagem que será enviada: {f}')
    Contagem = int(input(f'{azul}Quantas Vezes?: {f}'))
    print(f'{azul}**********************************************************{f}')

    valor =0
    nao_enviado =0
    connection = requests.sessions.Session()

    while valor < Contagem:

        headers = {
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'username': f'{nglusername}',
            'question': f'{mensagem}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        response = connection.post('https://ngl.link/api/submit', headers=headers, data=data)

        if response.status_code == 200:
            nao_enviado = 0
            valor += 1
            print(f'{v}[+]{f}Enviado =>{v}{valor}{f}')
        else:
            nao_enviado += 1
            print(f'{vermelho}[-]{f}Não Enviado')

        if nao_enviado == 10:
            print(f'{vermelho}[!]{f}Aguarde 5 Segundos')
            time.sleep(5)
            nao_enviado = 0

    connection.close()
    print(f'{amarelo}Projeto by {f}{ciano}@wandson.dev 🤠{f}')

ngl()