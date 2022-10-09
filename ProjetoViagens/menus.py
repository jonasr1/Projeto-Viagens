
def menuPrincipal():
    print("\n")
    print("-="*4,'MENU',"-="*4)
    print("\n")
    print('[1] - Menu de Motorista')
    print('[2] - Menu de Veiculo')
    print('[3] - Menu de Viagem')
    print('[4] - SAIR')
    opcao = int(input("Digite uma opção: "))
    return opcao


def menu_motorista():
    print("\n")
    print("-="*4,'MENU MOTORISTAS',"-="*4)
    print("\n")
    print("[1] - Cadastrar Motorista")
    print('[2] - Buscar Motorista por cpf')
    print('[3] - Editar Nome do Motorista')
    print('[4] - Remover Motorista')
    print('[5] - Listar os Motorista por tipo da carteira')
    print('[6] - Listar Todos os Motorista')
    print('[7] - SAIR')
    opcao=int(input('Digite uma opção:'))
    return opcao


def menu_veiculo():
    print("\n")
    print("-="*4,'MENU DE VEICULOS',"-="*4)
    print("\n")
    print('[1] - Cadastrar Veiculo')
    print('[2] - Buscar Veiculo por Placa')
    print('[3] - Adicionar motorista ao veiculo')
    print('[4] - Remover motorista do veiculo')
    print('[5] - Listar veiculos com motoristas')
    print('[6] - Listar veiculos sem motoristas')
    print('[7] - Remover Veiculo')
    print('[8] - SAIR')
    opcao=int(input("Digite uma opção:"))
    return opcao

def menu_viagem():
    print("\n")
    print("-"*8,"Menu de Viagem","-"*8)
    print("\n")
    print("1- Criar Viagem")
    print("2- Finalizar Viagem por placa")
    print("3- Viagens Ativas")
    print("4- Veiculos que estão em Viagem")
    print("5- Veiculos que estão Disponíveis para Viagem")
    print("6- Listar todas as Viagens")
    print("7- Listar todas as viagens por período")
    print("8- Sair")
    opcao=int(input("Digite a opção:"))
    return opcao

