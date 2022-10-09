from controlador_motorista import *
from controlador_veiculo import *
from menus import *
from controlador_viagem import *



def menu_viagens_funcoes():

    while True:
        opcao_menu = menu_viagem()
        if opcao_menu == 1:
            criarViagens()
        elif opcao_menu == 2:
            finalizarPorPlaca()
        elif opcao_menu ==3:
            viagensAtivas()
        elif opcao_menu == 4:
            veiculosEmViagens()
        elif opcao_menu == 5:
            veiculosDisponniveis()
        elif opcao_menu == 6:
            listarTodasViagens()
        elif opcao_menu == 7:
            listarPorPeriodo()
        elif opcao_menu == 8:
            break

def menu_veiculo_funcoes():
    while True:
        opcao_menu = menu_veiculo()
        if opcao_menu == 1:
            cadastrar_veiculo()
        elif opcao_menu == 2:
            buscar_veiculo()
        elif opcao_menu == 3:
            adicionar_motorista_ao_veiculo()
        elif opcao_menu == 4:
            remover_motorista_do_veiculo()
        elif opcao_menu == 5:
            listar_veiculos_com_motorista()
        elif opcao_menu == 6:
            listar_veiculos_sem_motoristas()
        elif opcao_menu == 7:
            excluirVeiculo()
        elif opcao_menu == 8:
            break

def menu_mot():
    while True:
        opcao_menu = menu_motorista()
        if opcao_menu == 1:
            cadastrar_motorista()
        elif opcao_menu == 2:
            buscar_motorista_cpf()
        elif opcao_menu == 3:
            editar_motorista()
        elif opcao_menu==4:
            remover_motorista()
        elif opcao_menu == 5:
            listar_tipo_CNH()
        elif opcao_menu == 6:
            listar_motoristas()
        elif opcao_menu == 7:
            break

def menu1():
    while True:
        opcao_menu = menuPrincipal()
        if opcao_menu == 1:
            menu_mot()
        elif opcao_menu == 2:
            menu_veiculo_funcoes()
        elif opcao_menu == 3:
            menu_viagens_funcoes()
        elif opcao_menu == 4:
            print()
            print("Programa Finalizado!!!")
            break


menu1()

