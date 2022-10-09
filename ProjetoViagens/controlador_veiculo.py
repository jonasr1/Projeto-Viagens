import json
import os
from controlador_motorista import *

arqBaseVeiculos = "bd_veiculos.json"

dados_veiculo = {}


def gravarDadosVeiculos():
    with open('bd_veiculos.json', 'w') as arqJson:
        json.dump(dados_veiculo, arqJson, indent=3)


def lerDadosVeiculos():
    with open('bd_veiculos.json', 'r+') as arqJson:
        global dados_veiculo
        dados_veiculo = json.load(arqJson)


def carregarDadosVeiculos():
    if os.path.exists(arqBaseVeiculos):
        with open(arqBaseVeiculos, 'r+') as arqJson:
            global dados_veiculo
            dados_veiculo = json.load(arqJson)


carregarDadosVeiculos()


def cadastrar_veiculo():
    print("\n", "-=" * 4, "Cadastrar Veiculo", "-=" * 4, "\n")
    while True:
        placa = input("Digite a placa do veiculo:").upper()
        escolha = int(input("Qual tipo do veiculo [1- MOTO 2- CARRO]:"))
        if escolha == 1:
            tipo = 'MOTO'
        elif escolha == 2:
            tipo = 'CARRO'
        else:
            print("\nOpção Inválida!!!\nPressione Enter para continuar!!!")
            input()
            break

        veiculo = {'Placa': placa, 'Tipo': tipo, 'MotoristaN': None}
        dados_veiculo[placa] = veiculo
        gravarDadosVeiculos()
        opcao = int(input("Deseja Cadastrar outro veiculo [1- Sim | 2- Não]:"))
        if opcao != 1:
            break


def buscar_veiculo():
    lerDadosVeiculos()
    print("\n", "-=" * 4, "Buscar Veiculo por Placa", "-=" * 4, "\n")
    placa = input("Digite a Placa do Veiculo:").upper()
    if placa in dados_veiculo:
        for veiculo in dados_veiculo.values():
            if veiculo.get('Placa') == placa:
                print()
                print('{:<12}''{:<12}''{:<12}'.format('Placa', 'Tipo','Motorista'))
                print('{:<12}''{:<12}''{:<12}'.format(veiculo.get('Placa'), veiculo.get('Tipo'), veiculo.get('MotoristaN')))
                print()
                print("Pressione qualquer tecla para continuar!")
                input()
                return
    else:
        print("\nVeiculo não encontrado!!!\nPressione qualquer tecla para continuar!")
        input()


def adicionar_motorista_ao_veiculo():
    print("\n", "-=" * 4, "Adicionar Motorista ao Veiculo", "-=" * 4, "\n")
    while True:
        lerDadosVeiculos()
        placa = input("Digite a placa do Veiculo que deseja adicionar o Motorista:").upper()
        if placa in dados_veiculo:
            for veiculo in dados_veiculo.values():
                if veiculo.get('Placa') == placa and veiculo.get('MotoristaN')is None:
                    cpf = input("Digite o CPF do motorista que deseja adiciona ao veiculo:")
                    for motorista in dados_motorista.values():
                        if cpf in motorista['CPF']:
                            for piloto in dados_motorista.values():
                                if piloto.get('CPF') == cpf:
                                    motorista = dados_motorista[cpf]
                                    motoristaAdicionar = motorista.get('Nome')
                                    veiculo = dados_veiculo[placa]
                                    tipo = veiculo.get('Tipo')
                                    veiculo = {'Placa': placa, 'Tipo': tipo, 'MotoristaN': motoristaAdicionar}
                                    dados_veiculo[placa] = veiculo
                                    gravarDadosVeiculos()
                                    opcao = int(input("Deseja adicionar outro motorista [1- Sim | 2-Não]:"))
                                    if opcao != 1:
                                        print("\nMotorista(s) adicionado(s) com sucesso!!!\nPressione qualquer tecla para continuar!")
                                        input()
                                        return
                    else:
                        print("\nMOTORISTA NÃO ENCONTRADO!!!\nPressione qualquer tecla para continuar!")
                        input()
                        return

            print("\nO VEICULO JÁ POSSUI MOTORISTA!!!\nPressione qualquer tecla para continuar!")
            input()
            return
        else:
            print("\nVeiculo não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()
            return


def remover_motorista_do_veiculo():
    print("\n", "-=" * 4, " Remover Motorista do Veiculo", "-=" * 4, "\n")
    while True:
        lerDadosVeiculos()
        placa = input("Digite a placa do Veiculo que deseja remover do Motorista:").upper()
        if placa in dados_veiculo:
            for veiculo in dados_veiculo.values():
                if veiculo.get('Placa') == placa:

                    if veiculo.get('MotoristaN') is not None:
                        cpf = input("Digite o CPF do motorista que deseja remover do veiculo:")
                        for motorista in dados_motorista.values():
                            if cpf in motorista['CPF']:
                                for piloto in dados_motorista.values():
                                    if piloto.get('CPF') == cpf:
                                        motorista = dados_motorista[cpf]
                                        motoristaAdicionar = None
                                        veiculo = dados_veiculo[placa]
                                        tipo = veiculo.get('Tipo')
                                        veiculo = {'Placa': placa, 'Tipo': tipo, 'MotoristaN': motoristaAdicionar}

                                        dados_veiculo[placa] = veiculo
                                        gravarDadosVeiculos()
                                        print("\nMotorista removido com sucesso!!!\n")

                                        opcao = int(input("Deseja remover outro motorista [1- Sim | 2-Não]:"))
                                        if opcao != 1:
                                            return

                        print("\nVEICULO NÃO ENCONTRADO!!!\nPressione qualquer tecla para continuar!")
                        input()
                        return
                    else:
                        print("\nO VEICULO NÃO POSSUI MOTORISTA!!!\nPressione qualquer tecla para continuar!")
                        input()
                        return

            print("\nVeiculo não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()
            return


def listar_veiculos_com_motorista():
    lerDadosVeiculos()
    print("\n", "-=" * 4, "Lista Veiculos com motoristas", "-=" * 4, "\n")
    for veiculoCom in dados_veiculo.values():
        if veiculoCom.get('MotoristaN') is not None:
            print("-" * 35)
            print('{:<12}''{:<12}''{:30}'.format('Placa', 'Tipo', 'Motorista'))
            print('{:<12}''{:<12}''{:30}'.format(veiculoCom.get('Placa'), veiculoCom.get('Tipo'),
                                                 veiculoCom.get('MotoristaN')))
    print()
    input("Pressione Enter para continuar!!!")
    return


def listar_veiculos_sem_motoristas():
    lerDadosVeiculos()
    print("\n", "-=" * 4, "Lista Veiculos sem motoristas", "-=" * 4, "\n")
    for veiculoSem in dados_veiculo.values():
        if veiculoSem.get('MotoristaN') is None:
            print("-" * 35)
            print('{:<12}''{:<12}''{:<30}'.format('Placa', 'Tipo', 'Motorista'))
            print('{:<12}''{:<12}''{:<30}'.format(veiculoSem.get('Placa'), veiculoSem.get('Tipo'), 'None'))

    print()
    input("Pressione Enter para continuar!!!")
    return


def excluirVeiculo():
    print("\n", "-=" * 4, "Remover Veiculo", "-=" * 4, "\n")
    while True:
        lerDadosVeiculos()
        placa = input("Digite Placa do Veiculo:").upper()
        if placa in dados_veiculo:
            for veiculo in dados_veiculo.values():
                if veiculo.get('Placa') == placa:
                    print('{:<12}''{:<12}'.format('Placa', 'Tipo'))
                    print('{:<12}''{:<12}'.format(veiculo.get('Placa'), veiculo.get('Tipo')))
                    print()
                    opcao = int(input("Deseja excluir o veiculo acima [1- Sim | 2- Não]:"))
                    if opcao == 1:
                        del dados_veiculo[placa]
                        gravarDadosVeiculos()
                        print("Veiculo Removido com Sucesso!!!\nPressione Enter para continuar!")
                        input()
                        escolha = int(input("Deseja Remover outro veiculo [1- Sim | 2- Não]:"))
                        if escolha != 1:
                            return
                    else:
                        return
        else:
            print("Veiculo Não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()
