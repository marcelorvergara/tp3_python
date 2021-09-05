import threading


class Questao7(threading.Thread):
    def __init__(self):
        super().__init__()
        i = ''
        lista = []
        while i != 'd':
            print("Fundamentod de Python")
            print("Teste de Performance - TP3")
            print("\t")
            print("Escolha uma opção: ")

            print("\t")
            print("Opçao a - Mostrar lista")
            print("Opçao b - Incluir elemento")
            print("Opçao c - Remover elemento")
            print("Opçao d - Limpar a lista e SAIR")

            entrada = True

            while entrada:
                try:
                    i = input("Digite aqui a opção escolhida: ")
                    if i == 'a':
                        print("Conteúdo da lista\n", lista)
                    elif i == 'b':
                        addElem = input("Digite o elemento que deseja incluir na lista\n")
                        lista.append(addElem)
                    elif i == 'c':
                        delElem = input("Entre com o valor do elemento que deseja remover da lista\n")
                        lista.remove(delElem)
                    elif i == 'd':
                        lista.clear()
                        if len(lista) == 0:
                            print("Operção concluída com sucesso!")
                        entrada = False
                except:
                    print("Entrada inválida!")
