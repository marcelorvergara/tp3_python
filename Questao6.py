import threading


class Questao6(threading.Thread):
    def __init__(self):
        super().__init__()
        frase = ""
        frases = []
        while frase != "Sair":
            frase = input("Digite uma frase e \'Sair\' para sair\n")
            match = frase.find("eu")
            if not match:
                frases.append(frase)
        print("Foram encontradas as seguintes frases com a palavra \'eu\'")
        for i in frases:
            print(i)
