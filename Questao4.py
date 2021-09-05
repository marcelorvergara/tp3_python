import threading


class Questao4(threading.Thread):
    def __init__(self):
        super().__init__()
        qtd_nums = int(input("Entre com a quantidade de números que deseja entrar:"))
        nums = []
        for i in range(qtd_nums):
            num = int(input("Número " + str(i+1) + ": "))
            if num == 0:
                nums.append(num)
        print("A quantidade de números zeros é: ", len(nums))
