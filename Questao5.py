import threading


class Questao5(threading.Thread):

    alunos_alturas = {}
    soma_alturas = 0

    def __init__(self):
        super().__init__()
        print("Entre com o nome do(a) aluno(a) e, em seguida, sua altura.\nEntre \"Sair\" para sair :")
        nome = ''
        altura = ''
        mat = 1
        while True:
            nome = input("Entre com o nome do aluno: ")
            if nome == 'Sair':
                break
            altura = input("Entre com sua altura: ")
            if altura == 'Sair':
                break
            try:
                # uso do mat para homônimos
                float_altura = float(altura)
                self.alunos_alturas[str(mat) + ' - ' + nome] = float_altura
                self.soma_alturas += float_altura
                mat += 1
            except ValueError:
                print("Altura inválida. A altura deve conter somente números.")
        self.alunos_altos()

    def alunos_altos(self):
        media = self.soma_alturas / len(self.alunos_alturas)
        print("Alunos que possuem altura maior que a média " + str(round(media,2)) + " da turma:")
        for aluno, altura in self.alunos_alturas.items():
            if altura>media:
                print(aluno)
