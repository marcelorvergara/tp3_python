from threading import Thread


import MenuItems
from Questao1 import Questao1
from Questao2 import Questao2
from Questao3 import Questao3
from Questao4 import Questao4
from Questao5 import Questao5
from Questao6 import Questao6
from Questao7 import Questao7
from Questao8 import Questao8
from Questao9Desafio import Questao9Desafio


def switch_menu(arg):
    if arg == 1:
        qst = Questao1()
        qst.start()
    elif arg == 2:
        qst = Questao2()
        qst.start()
    elif arg == 3:
        qst = Questao3()
        qst.start()
    elif arg == 4:
        qst = Questao4()
        qst.start()
    elif arg == 5:
        qst = Questao5()
        qst.start()
    elif arg == 6:
        qst = Questao6()
        qst.start()
    elif arg == 7:
        qst = Questao7()
        qst.start()
    elif arg == 8:
        qst = Questao8()
        qst.start()
    elif arg == 9:
        qst = Questao9Desafio()
        qst.start()
    elif arg == 0:
        print("")
    else:
        print("\n--------\nQuestão inexistente ou opção inválida!\n--------\n")


def main_menu():
    num = 0
    ent_ok = False
    while not ent_ok:
        try:
            menu_loop = False
            while not menu_loop:
                menu_items = MenuItems.MenuItems()
                menu_items.start()
                num = int(input("Entre com o número da questão: "))
                if num == 0:
                    menu_loop = True
                    print("Inté!")
                switch_menu(num)
                print()
                ent_ok = True
        except ValueError:
            print('\n-----------------\nEntrada inválida!\n-----------------')
    return num


main_menu()
