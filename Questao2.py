import threading


class Questao2(threading.Thread):
    def __init__(self):
        super().__init__()
        print("Digite 5 números inteiros")
        nums = []
        for i in range(1,6):
            num = int(input("Número " + str(i) + ": "))
            nums.append(num)
        print(nums)
