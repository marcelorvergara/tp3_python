import os
import random
import secrets
import time
from tkinter import *

pri_tentativa = 0
times = 0


class Questao9Desafio:

    def __init__(self, master):
        self.master = master
        self.num_tentativas = 0
        self.gabarito = {}
        self.matriz = []
        self.viradas = []
        self.matriz_viradas = []
        self.mins = StringVar()
        self.sec = StringVar()
        Button(self.master, text='Começar', bd='2', bg='IndianRed1', font=('Helveticabold', 10),
               command=lambda: self.inicia()).place(x=60, y=60)

    def on_click(self, event):
        global pri_tentativa, times
        num = event.widget.cget('image').split('pyimage')[1]
        num_int = int(num)
        # não é primeira tentativa
        if pri_tentativa != 0:
            # testar se acertou
            tentativa_2 = self.gabarito[num_int]
            tentativa_1 = self.gabarito[pri_tentativa]
            if tentativa_1 == tentativa_2:
                print('acertou mezerávi')
                # acertou
                self.img_default(tentativa_1, '', '')
            else:
                # virar de volta a primeira tentativa
                self.img_default('', '', '')
            # zerar as tentativas
            pri_tentativa = 0
        # primeira tentativa
        else:
            # virar a carta da primeira tentativa para verificar se acertou
            self.img_default('', event.widget.cget('image'), self.gabarito[num_int])
            pri_tentativa = num_int
        # verifica se ganhou
        if len(self.viradas) == 12:
            times = -1
            print('Ganhou', 60 - int(self.sec.get()))
            tempo = 60 - int(self.sec.get())
            msg = text = "Você ganhou com o tempo de: " + str(tempo) + " segundos"
            res_window = Toplevel(self.master)
            app = Resultado(res_window, msg)

    def img_default(self, virada, pri_clique, nome_pri_clique):
        # virada -> nome da dupla de cartas que user acertou (ex: python.png)
        # pri_clique -> primeiro clique (ex: pyimage9)
        idx = 1
        for ii in range(3):
            for jj in range(4):
                # acertou mizerávi
                if virada == self.matriz[ii][jj]:
                    # grava o endereço da segunda da dupla que acertou
                    self.matriz_viradas.append([ii, jj])
                    # grava o nome da dupla que acertou
                    self.viradas.append(self.matriz[ii][jj])
                    label_ok = Label(self.master, image='')
                    pricture_ok = PhotoImage(file=os.path.join('logos', virada))
                    label_ok.img = pricture_ok
                    label_ok.config(image=label_ok.img)
                    label_ok.grid(row=ii, column=jj)
                # virar a primeira da dupla que acertou. A segunda foi virada no primeiro if acima
                elif self.matriz[ii][jj] in self.viradas and [ii, jj] not in self.matriz_viradas:
                    label_ok = Label(self.master, image='')
                    pricture_ok = PhotoImage(file=os.path.join('logos', virada))
                    label_ok.img = pricture_ok
                    label_ok.config(image=label_ok.img)
                    label_ok.grid(row=ii, column=jj)
                # cria o botão sem imagem para clicar
                elif self.matriz[ii][jj] not in self.viradas:
                    b = Button(self.master, image='')
                    nome_carta = 'pyimage' + str(idx)
                    if nome_carta == pri_clique:
                        # primeiro clique, manter virada
                        label_pri = Label(self.master, image='')
                        pricture_pri = PhotoImage(file=os.path.join('logos', nome_pri_clique))
                        label_pri.img = pricture_pri
                        label_pri.config(image=label_pri.img)
                        label_pri.grid(row=ii, column=jj)
                    else:
                        picture_d = PhotoImage(file='img_virada.png', name=nome_carta)
                        b.img = picture_d
                        b.config(image=b.img)
                        b.grid(row=ii, column=jj)
                        b.bind('<Button-1>', self.on_click)
                idx += 1

    def inicia(self):
        global times
        self.num_tentativas = 0
        self.gabarito = {}
        self.matriz = []
        self.viradas = []
        self.matriz_viradas = []
        logos_files = os.listdir("logos")
        random_files = random.sample(logos_files, 6)
        random_files_2 = random_files
        joined_files = random_files_2 + random_files

        # criar tabela com imagens randómicas
        for l in range(3):
            linha = []
            for c in range(4):
                ran = secrets.choice(joined_files)
                joined_files.remove(ran)
                linha.append(ran)
            self.matriz.append(linha)

        # colocando as imagens da tabela no tela
        tot = 0
        gabarito_l = {}
        for i in range(3):
            for j in range(4):
                b = Label(self.master, image='')
                picture = PhotoImage(file=os.path.join('logos', self.matriz[i][j]))
                gabarito_l[tot + 1] = self.matriz[i][j]
                self.gabarito.update(gabarito_l)
                b.img = picture
                b.config(image=b.img)
                b.grid(row=i, column=j)
                tot += 1
        # minutos e segundos no cando inferior
        lbl_mins = Entry(self.master, textvariable=self.mins, width=2)
        lbl_mins.grid(row=3, column=1)
        lbl_sec = Entry(self.master, textvariable=self.sec, width=2)
        lbl_sec.grid(row=3, column=2)
        # 5 segundos para memorizar
        self.master.after(5000, self.img_default, '', '', '')
        # contador de tempo para memorização
        self.mins.set('00')
        self.sec.set('05')
        times = int(self.mins.get()) * 60 + int(self.sec.get())
        while times > -1:
            minute, second = (times // 60, times % 60)
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)
            self.sec.set(second)
            self.mins.set(minute)
            # Update tempo
            self.master.update()
            time.sleep(1)
            if times == 0:
                self.sec.set('00')
                self.mins.set('00')
            times -= 1
        # contador de tempo para resolução
        self.mins.set('01')
        self.sec.set('00')
        times = int(self.mins.get()) * 60 + int(self.sec.get())
        while times > -1:
            minute, second = (times // 60, times % 60)
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)
            self.sec.set(second)
            self.mins.set(minute)
            # Update tempo
            self.master.update()
            time.sleep(1)
            if times == 0:
                self.sec.set('00')
                self.mins.set('00')
            times -= 1
        if len(self.viradas) < 12:
            times = -1
            res_window = Toplevel(self.master)
            app = Resultado(res_window, 'Você não ganhou :-(')


class Resultado:
    def __init__(self, master, msg):
        self.master = master
        self.frame = Frame(self.master)
        self.msg = Label(self.frame, text=msg, font=('Helveticabold', 14)).grid(sticky=W, row=1, column=1, padx=15, pady=12)
        self.close = Button(self.frame, text='Fechar o Jogo', bd='2', bg='IndianRed1', font=('Helveticabold', 10),
                            command=self.fecha_janela).grid(sticky=E, row=5, column=1, padx=5, pady=2)
        self.novo = Button(self.frame, text='Tentar Novamente', bd='2', bg='IndianRed1', font=('Helveticabold', 10),
                           command=self.tenta_novamente).grid(sticky=E, row=6, column=1, padx=5, pady=2)
        self.frame.grid()

    def fecha_janela(self):
        self.master.destroy()
        root.update()
        root.destroy()

    def tenta_novamente(self):
        for child in root.winfo_children():
            child.destroy()
        q = Questao9Desafio(root)
        root.update()
        self.master.destroy()
        root.after(100, q.inicia())


def saindo():
    root.destroy()


def main():
    global root
    root = Tk()
    root.protocol('WM_DELETE_WINDOW', saindo)
    root.title("Teste de Memória")
    q9 = Questao9Desafio(root)
    root.mainloop()


if __name__ == "__main__":
    main()
