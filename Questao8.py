import threading
from random import randrange


class Questao8(threading.Thread):
    def __init__(self):
        super().__init__()
        print("Questão 8")
        resultados = [0, 0, 0, 0, 0, 0, 0]
        i = 0
        while i < 100:
            dado = randrange(1, 7)
            resultados[dado] = resultados[dado] + 1
            i += 1
        n = 0
        for n in range(1, len(resultados)):
            print("O número", n, " saiu", resultados[n], " vezes")
