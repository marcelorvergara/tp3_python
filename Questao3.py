import threading


class Questao3(threading.Thread):
    def __init__(self):
        super().__init__()
        print("Digite 10 palavras")
        palavras = []
        for i in range(10):
            palavra = input("Palavra " + str(i+1) + ": ")
            palavras.append(palavra)
        for i in reversed(palavras):
            print(i)
