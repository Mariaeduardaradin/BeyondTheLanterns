import os
import json
from datetime import datetime

def limpar_tela():
    os.system("cls")

def inicializar_log():
    try:
        banco = open("log.dat", "r")
    except:
        print("Banco de Dados Inexistente. Criando...")
        banco = open("log.dat", "w")

def salvar_log(nome, pontos):
    banco = open("log.dat", "r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    dadosDict[nome] = (pontos, data, hora)

    banco = open("log.dat", "w")
    banco.write(json.dumps(dadosDict))
    banco.close()

def maior_pontuador():
    banco = open("log.dat", "r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    maiorNome = "Sem Jogador"
    maiorPontos = 0
    dataJogada = "--"
    horaJogada = "--"

    for nome, info in dadosDict.items():

        pontos = info[0]

        if pontos > maiorPontos:
            maiorPontos = pontos
            maiorNome = nome
            dataJogada = info[1]
            horaJogada = info[2]
            
    return maiorNome, maiorPontos, dataJogada, horaJogada