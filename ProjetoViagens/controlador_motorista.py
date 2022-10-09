
dados_motorista ={}
import json
import os
arqBase="bd_motorista.json"


def gravarDados ():
    with open('bd_motorista.json', 'w') as arqJson:
        json.dump(dados_motorista, arqJson, indent=3)

def lerDadosMotorista():
    with open('bd_motorista.json','r+') as arqJson:
        global dados_motorista
        dados_motorista = json.load(arqJson)

def carregarDadosMotorista():
    if os.path.exists(arqBase):
        with open(arqBase,'r+') as arqJson:
            global dados_motorista
            dados_motorista=json.load(arqJson)

carregarDadosMotorista()

def cadastrar_motorista():

    print("\n","-="*4,"Cadastrar Motorista","-="*4,"\n")
    while True:
        nome = str(input("Digite o nome: "))
        cpf= input("Digite o CPF: ")
        if cpf in dados_motorista:
            print()
            print("Motorista já Cadastado!!!")
            input("Digite Enter Para continuar!!!")
            break
        tipo = int(input("Qual carteira o motorista possui? [1]-A [2]-B [3]-AB: "))
        if tipo == 1:
            cnh = 'A'
        elif tipo == 2:
            cnh = 'B'
        elif tipo == 3:
            cnh = 'AB'
        else:
            print("\nOpção Inválida!!!\nPressione Enter para continuar!!!")
            input()
            break
        motorista={'CPF':cpf,'Nome':nome,'CNH':cnh}
        dados_motorista[cpf]=motorista
        gravarDados()
        opcao = int(input("Deseja cadastrar outro motorista: [1]-SIM  [2]-NÃO :"))

        if opcao != 1:
            break


def buscar_motorista_cpf():
    print("\n", "-=" * 4, "Buscar Motorista", "-=" * 4, "\n")
    while True:
        lerDadosMotorista()
        cpf=input("Digite o CPF do Motorista:")
        if cpf in dados_motorista:
            for motorista in dados_motorista.values():
                if motorista.get('CPF')==cpf:
                    print()
                    print('{:<12}''{:<12}''{:30}'.format('CPF', 'Nome', 'CNH'))
                    print('{:<12}''{:<12}''{:30}'.format(motorista.get('CPF'),motorista.get('Nome'),motorista.get('CNH')))
                    opcao = int(input("Deseja cadastrar outro veiculo [1- Sim | 2-Não]:"))
                    if opcao != 1:
                        break
        else:
            print("Motorista não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()

def editar_motorista():
    print("-=" * 4, "Editar Nome do Motorista", "-=" * 4)
    while True:
        lerDadosMotorista()
        cpf=input("Digite o CPF do Motorista:")
        if cpf in dados_motorista:
            for motorista in dados_motorista.values():
                if motorista.get('CPF')==cpf:
                    novoNome=input("Digite o novo nome:")
                    motorista={'CPF':cpf,'Nome':novoNome}
                    dados_motorista[cpf]=motorista
                    gravarDados()
                    opcao = int(input("Deseja editar outro veiculo [1- Sim | 2-Não]:"))
                    if opcao != 1:
                        break
                    print()
                    print("Nome(s) Editado(s) com sucesso!!!\nPressione qualquer tecla para continuar!")
                    input()
                    return
        else:
            print("Motorista não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()


def remover_motorista():
    print("\n", "-=" * 4, "Remover Motorista", "-=" * 4, "\n")
    while True:
        lerDadosMotorista()
        cpf=input("Digite o CPF do Motorista:")
        if cpf in dados_motorista:
            for motorista in dados_motorista.values():
                if motorista.get('CPF')==cpf:
                    print('{:<12}''{:<12}''{:30}'.format('CPF', 'Nome', 'CNH'))
                    print('{:<12}''{:<12}''{:30}'.format(motorista.get('CPF'), motorista.get('Nome'), motorista.get('CNH')))
                    print()
                    opcao=int(input("Deseja excluir o Motorista acima [1- Sim | 2- Não]:"))
                    if opcao==1:
                        del dados_motorista[cpf]
                        gravarDados()
                        print("\nMotorista Excluido com Sucesso!!!\n")

                        opcao = int(input("Deseja exluir outro motorista [1- Sim | 2-Não]:"))
                        if opcao != 1:
                            return

        else:
            print("Motorista não encontrado!!!\nPressione qualquer tecla para continuar!")
            input()
            return

def listar_tipo_CNH():
    lerDadosMotorista()
    print("\n","-="*4,"Lista por tipo de Carteira","-="*4,"\n")
    escolha=int(input("Deseja listar por [1- Tipo A | 2- Tipo B | 3- Tipo AB]:"))
    if escolha == 1:
        print("\n","-="*5,"Tipo A","-="*5,"\n")
        print('{:<12}''{:<12}''{:30}'.format('CPF', 'Nome', 'CNH'))
        for motorista in dados_motorista.values():
            if motorista.get('CNH')=='A':
                print('{:<12}''{:<12}''{:30}'.format(motorista.get('CPF'), motorista.get('Nome'), motorista.get('CNH')))
        print()
        input("Pressione Enter para continuar!!!")
        return
    if escolha ==2:
        print("\n","-=" * 5, "Tipo B", "-=" * 5, "\n")
        print('{:<12}''{:<12}''{:30}'.format('CPF', 'Nome', 'CNH'))
        for motorista in dados_motorista.values():
            if motorista.get('CNH') == 'B':
                 print('{:<12}''{:<12}''{:30}'.format(motorista.get('CPF'), motorista.get('Nome'), motorista.get('CNH')))
        print()
        input("Pressione Enter para continuar!!!")
        return
    if escolha == 3:
        print("\n","-=" * 5, "Tipo AB", "-=" * 5, "\n")
        print('{:<12}''{:<12}''{:30}'.format('CPF', 'Nome', 'CNH'))
        for motorista in dados_motorista.values():
            if motorista.get('CNH') == 'AB':
                print('{:<12}''{:<12}''{:30}'.format(motorista.get('CPF'), motorista.get('Nome'), motorista.get('CNH')))
                print()
        input("Pressione Enter para continuar!!!")
        return


def listar_motoristas ():
    lerDadosMotorista()
    print("\n")
    print("-=" * 4, "Lista de Motoristas", "-=" * 4)
    print()
    print('{:<12}''{:<12}''{:<30}'.format('CPF', 'Nome', 'CNH'))
    for motorista in dados_motorista.values():
        print('{:<12}''{:<12}''{:<30}'.format(motorista.get('CPF'), motorista.get('Nome'),motorista.get('CNH')))
    print()
    input("Aperte Enter para continuar!")






