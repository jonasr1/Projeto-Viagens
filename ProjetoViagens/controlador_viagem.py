import json
import os
from controlador_veiculo import *
from datetime import datetime
import re

dados_viagens = {}

arqBaseViagens = "bd_viagens.json"


def gravarDadosViagens():
    with open('bd_viagens.json', 'w') as arqJson:
        json.dump(dados_viagens, arqJson, indent=4)


def lerDadosViagens():
    with open('bd_viagens.json', 'r+') as arqJson:
        global dados_viagens
        dados_viagens = json.load(arqJson)


def carregarDadosViagens():
    if os.path.exists(arqBaseViagens):
        with open(arqBaseViagens, 'r+') as arqJson:
            global dados_viagens
            dados_viagens = json.load(arqJson)


def obterViagem(placa):
    if placa in dados_viagens:
        print('Tamanho da lista:', len(dados_viagens[placa]))
        return dados_viagens[placa]


def converterEmData(string):
    string_fomatar = string.split('/')
    dia = int(string_fomatar[0])
    mes = int(string_fomatar[1])
    ano = int(string_fomatar[2])
    return datetime(day=dia, month=mes, year=ano).date()


carregarDadosViagens()


def criarViagens():
    print("\n", "-=" * 4, "Criar Viagens", "-=" * 4, "\n")
    while True:
        placa = input("Digite a placa do veiculo:").upper()
        if placa in dados_veiculo:
            for veiculo in dados_veiculo.values():
                if veiculo.get('Placa') == placa:
                    if veiculo.get('MotoristaN') is not None:
                        usuario = input("digite a data [ex: 21/03/2022]:")
                        valorCorreto = re.search(r'(\d{2})/(\d{2})/(\d{4})', usuario)
                        if valorCorreto:
                            converter = converterEmData(string=usuario)
                            convertida = str(converter)
                            print("Data convertida", converter)
                            veiculo = dados_veiculo[placa]
                            rota = input("Digite a rota:")
                            status = True
                            listaViagens = obterViagem(placa)
                            if listaViagens is None:
                                listaViagens = []
                            viagem = {placa: veiculo, 'rota': rota, 'status': status, 'data': convertida}
                            listaViagens.append(viagem)
                            dados_viagens[placa] = listaViagens

                            gravarDadosViagens()
                            opcao = int(input("Deseja criar outra viagem [1- Sim | 2-Não]:"))
                            if opcao != 1:
                                print("\nViagem(ns) criada(s) com sucesso!!!\nPressione qualquer tecla para continuar!")
                                input()
                                return
                        else:
                            print("Formato errado!!! O formato é:DIA/MÊS/ANO\nComece do inicio Pressionando Enter!!!")
                            input()
                    else:
                        print("\nO VEICULO NÃO POSSIU MOTORISTA!!!\nPressione qualquer tecla para continuar!")
                        input()
                        return
        else:
            print("\nVeiculo não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()
            return


def finalizarPorPlaca():
    global dados_viagens
    lerDadosVeiculos()
    print("\n", "-=" * 4, "Finalizar Viagem por placa", "-=" * 4, "\n")

    placa = input("Digite a placa do veiculo:").upper()
    if placa in dados_veiculo:

        for chave, viagens in dados_viagens.items():
            for viagem in viagens:

                if chave == placa:
                    veiculoN = dados_veiculo[placa]
                    rotaN = viagem.get('rota')
                    novostatus = False
                    dataN = viagem.get('data')
                    del dados_viagens[placa]
                    listaViagens = obterViagem(placa)
                    if listaViagens is None:
                        listaViagens = []
                    viagemF = {placa: veiculoN, 'rota': rotaN, 'status': novostatus, 'data': dataN}
                    listaViagens.append(viagemF)
                    dados_viagens[placa] = listaViagens
                    gravarDadosViagens()
                    print("\nViagem Finalizada com sucesso!!!\nPressione Enter para continuar!!!")
                    input()
                    return
    else:
        print("Veiculo não encontrado!!!\nPressione Enter para continuar!!!")
        input()
        return


def viagensAtivas():
    print("\n", "-=" * 4, "Viagens Ativas", "-=" * 4, "\n")
    lerDadosViagens()
    while True:
        for status, viagens in dados_viagens.items():
            for viagem in viagens:
                if viagem.get('status') is True:
                    print("-" * 35)
                    print("\nPlaca do veiculo:", viagem.get(status).get('Placa'))
                    print("Tipo do veiculo:", viagem.get(status).get('Tipo'))
                    print("Motorista do veiculo:", viagem.get(status).get('MotoristaN'))
                    print("Rota da Viagem:", viagem.get('rota'))
                    print("Data da Viagem:", viagem.get('data'))
                    print("Status da Viagem:", viagem.get('status'))
        input("\nPressione Enter para continuar!!!")
        return


def listarTodasViagens():
    print("\n", "-=" * 4, "Lista de Todas as Viagens", "-=" * 4, "\n")
    for placa, viagens in dados_viagens.items():
        if placa in dados_veiculo:
            for viagem in viagens:
                print("-" * 45)
                print("Placa do veiculo:", viagem.get(placa).get('Placa'))
                print("Tipo do veiculo:", viagem.get(placa).get('Tipo'))
                print("Motorista do veiculo:", viagem.get(placa).get('MotoristaN'))
                print("Rota da Viagem:", viagem.get('rota'))
                print("Data da viagem:", viagem.get('data'))
                print("Status da Viagem:", viagem.get('status'))
    input("\nPressione Enter para continuar!!!")
    return


def veiculosEmViagens():
    print("\n", "-=" * 4, "Veiculos em Viagens", "-=" * 4, "\n")
    for placa, viagens in dados_viagens.items():
        for viagem in viagens:
            print("-" * 35)
            print('{:<12}''{:<12}''{:<30}'.format('Placa', 'Tipo', 'Motorista'))
            print('{:<12}''{:<12}''{:<30}'.format(viagem.get(placa).get('Placa'), viagem.get(placa).get('Tipo'),
                                                  viagem.get(placa).get('MotoristaN')))
    input("\nPressione Enter para continuar!!!")
    return


def veiculosDisponniveis():
    print("\n", "-=" * 4, "Veiculos Disponíveis Para Viagem", "-=" * 4, "\n")
    for placa, veiculos in dados_veiculo.items():
        if placa not in dados_viagens.keys():
            print("-" * 35)
            print('{:<12}''{:<12}''{:<30}'.format('Placa', 'Tipo', 'Motorista'))
            print('{:<12}''{:<12}''{:<30}'.format(veiculos.get('Placa'), veiculos.get('Tipo'),
                                                  veiculos.get('MotoristaN')))
    input("\nPressione Enter para Continuar!!!")
    return


def listarPorPeriodo():
    print("\n", "-=" * 4, "Listar viagens por período", "-=" * 4, "\n")
    dataIncial = input("Digite a data inicíal [ex:27/03/2022]:")
    valorCorreto = re.search(r'(\d{2})/(\d{2})/(\d{4})', dataIncial)
    if valorCorreto:
        converter = converterEmData(string=dataIncial)
        convertidaI = str(converter)
    else:
        input("Formato errado!!! O formato é:DIA/MÊS/ANO\nComece do inicio Pressionando Enter!!!")
        return
    dataFinal = input("Digite a data final [ex:27/03/2022]:")
    valorCorreto = re.search(r'(\d{2})/(\d{2})/(\d{4})', dataFinal)
    if valorCorreto:
        converter = converterEmData(string=dataFinal)
        convertidaF = str(converter)
    else:
        input("Formato errado!!! O formato é:DIA/MÊS/ANO\nComece do inicio Pressionando Enter!!!")
        return

    for placa, viagens in dados_viagens.items():
        for viagem in viagens:
            if viagem.get('data') > convertidaI and viagem.get('data') < convertidaF:
                print("-" * 45)
                print("Placa do veiculo:", viagem.get(placa).get('Placa'))
                print("Tipo do veiculo:", viagem.get(placa).get('Tipo'))
                print("Motorista do veiculo:", viagem.get(placa).get('MotoristaN'))
                print("Rota da Viagem:", viagem.get('rota'))
                print("Data da viagem:", viagem.get('data'))
                print("Status da Viagem:", viagem.get('status'))
    print()
    input("Pressione Enter para continuar!!!")
    return
