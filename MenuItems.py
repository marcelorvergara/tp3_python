import threading


class MenuItems(threading.Thread):
    def __init__(self):
        super().__init__()
        print("\n-------Menu--------\n")
        print("1 - Manipulação de Listas")
        print("2 - Cinco vetores")
        print("3 - Vetor de dez palavras")
        print("4 - Qtd. zeros em núm. X")
        print("5 - Alunos: Nomes e Alturas")
        print("6 - Eu?")
        print("7 - Programa de Manipulação de Listas")
        print("8 - Vc tem dado em casa?")
        print("9 - Desafio\n")
        print("0 - Digite 0 (Zero) para sair\n")

