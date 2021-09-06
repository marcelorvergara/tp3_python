import os
import random
import secrets
import threading
import time
from tkinter import *

root = Tk()
root.title("Teste de Memória")

pri_tentativa = 0


class Questao9Desafio(threading.Thread):
    num_tentativas = 0
    gabarito = {}
    matriz = []
    viradas = []
    matriz_viradas = []
    mins = StringVar()
    sec = StringVar()

    def __init__(self):
        super().__init__()
        Button(root, text='Começar', bd='2', bg='IndianRed1', font=('Helveticabold', 10),
               command=lambda: self.inicia()).place(x=60, y=60)
        root.mainloop()

    def on_click(self, event):
        global pri_tentativa
        num = event.widget.cget('image').split('pyimage')[1]
        num_int = int(num)
        # não é primeira tentativa
        if pri_tentativa != 0:
            # testar
            tentativa_2 = self.gabarito[num_int]
            tentativa_1 = self.gabarito[pri_tentativa]
            if tentativa_1 == tentativa_2:
                print('acertou')
                # acertou
                self.img_default(tentativa_1)
            # zerar as tentativas
            pri_tentativa = 0
        # primeira tentativa
        else:
            pri_tentativa = num_int
        if len(self.viradas) == 12:
            print('Ganhou', 60 - int(self.sec.get()))
            tempo = 60 - int(self.sec.get())
            res_window = Toplevel(root)
            res_window.title('Resultado Vencedor!')
            res_window.geometry('750x240')
            Label(res_window, text="Você ganhou com o tempo de: " + str(tempo) + " segundos").place(x=167, y=80)

    def img_default(self, virada):
        idx = 1
        for ii in range(3):
            for jj in range(4):
                if virada == self.matriz[ii][jj]:
                    self.matriz_viradas.append([ii, jj])
                    self.viradas.append(self.matriz[ii][jj])
                    label_ok = Label(root, image='')
                    pricture_ok = PhotoImage(file='logos/' + virada)
                    label_ok.img = pricture_ok
                    label_ok.config(image=label_ok.img)
                    label_ok.grid(row=ii, column=jj)
                elif self.matriz[ii][jj] in self.viradas and [ii, jj] not in self.matriz_viradas:
                    label_ok = Label(root, image='')
                    pricture_ok = PhotoImage(file='logos/' + virada)
                    label_ok.img = pricture_ok
                    label_ok.config(image=label_ok.img)
                    label_ok.grid(row=ii, column=jj)
                elif self.matriz[ii][jj] not in self.viradas:
                    b = Button(root, image='')
                    picture_d = PhotoImage(file='img_virada.png', name='pyimage' + str(idx))
                    b.img = picture_d
                    b.config(image=b.img)
                    b.grid(row=ii, column=jj)
                    b.bind('<Button-1>', self.on_click)
                idx += 1

    def inicia(self):
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
                b = Label(root, image='')
                picture = PhotoImage(file='logos/' + self.matriz[i][j])
                gabarito_l[tot + 1] = self.matriz[i][j]
                self.gabarito.update(gabarito_l)
                b.img = picture
                b.config(image=b.img)
                b.grid(row=i, column=j)
                tot += 1
        lbl_mins = Entry(root, textvariable=self.mins, width=2)
        lbl_mins.grid(row=3, column=1)
        lbl_sec = Entry(root, textvariable=self.sec, width=2)
        lbl_sec.grid(row=3, column=2)
        root.after(5000, self.img_default, '')
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
            root.update()
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
            root.update()
            time.sleep(1)
            if times == 0:
                self.sec.set('00')
                self.mins.set('00')
            times -= 1
        if len(self.viradas) < 12:
            res_window = Toplevel(root)
            res_window.title('O Tempo acabou!')
            res_window.geometry('750x240')
            Label(res_window, text='Você não ganhou').place(x=10, y=10)
            Button(res_window, text='Tentar Novamente', bd='2', bg='IndianRed1', font=('Helveticabold', 10),
                   command=lambda: self.inicia()).place(x=60, y=60)


if __name__ == "__main__":
    Questao9Desafio = Questao9Desafio()
    Questao9Desafio.mainloop()
