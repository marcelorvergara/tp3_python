import threading


class Questao1(threading.Thread):
    def __init__(self):
        super().__init__()
        # Usando python, faça  o que se pede:
        # 1.1 - Crie uma lista vazia
        lista = []
        # 1.2 - Adicione os elementos 1, 2, 3, 4 ,5 usando append()
        for i in range(5):
            lista.append(i + 1)
        # 1.3 - Imprima a lista
        print(lista)
        # 1.4 - Remova os elementos 3 e 6 checando se eles estão na lista
        try:
            lista.pop(2)
            print("Elemento 3 excluído com sucesso")
        except IndexError:
            print("Elemento 3 inexistente")
        try:
            lista.pop(5)
            print("Elemento 6 excluído com sucesso")
        except IndexError:
            print("Elemento 6 não existe")
        # 1.5 - Imprima a lista
        print(lista)
        # 1.6 - Imprima o tamanho da lista com len
        print("O tamanho da lista é", len(lista))
        # 1.7 - Altere o último elemento da lista para 6 e imprima a lista modificada
        lista[len(lista) - 1] = 6
        print(lista)
