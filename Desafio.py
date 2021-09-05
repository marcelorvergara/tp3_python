import os, time
import random
import secrets
from tkinter import *

root = Tk()
root.title("Teste de Memória")

num_tentativas = 0
gabarito = {}
pri_tentativa = 0
matriz = []
viradas = []
matriz_viradas = []
mins = StringVar()
sec = StringVar()


def on_click(event):
    global pri_tentativa
    num = event.widget.cget('image').split('pyimage')[1]
    num_int = int(num)
    # não é primeira tentativa
    if pri_tentativa != 0:
        # testar
        tentativa_2 = gabarito[num_int]
        tentativa_1 = gabarito[pri_tentativa]
        if tentativa_1 == tentativa_2:
            print('acertou')
            # acertou
            img_default(tentativa_1)
        # zerar as tentativas
        pri_tentativa = 0
    # primeira tentativa
    else:
        pri_tentativa = num_int
    if len(viradas) == 12:
        print('Ganhou', 60 - int(sec.get()))
        tempo = 60 - int(sec.get())
        res_window = Toplevel(root)
        res_window.title('Resultado Vencedor!')
        res_window.geometry('750x240')
        Label(res_window, text='Você ganhou com o tempo de: ' + str(tempo) + " segundos").place(x=167, y=80)


def img_default(virada):
    idx = 1
    for ii in range(3):
        for jj in range(4):
            if virada == matriz[ii][jj]:
                matriz_viradas.append([ii, jj])
                viradas.append(matriz[ii][jj])
                label_ok = Label(root, image='')
                pricture_ok = PhotoImage(file='logos/' + virada)
                label_ok.img = pricture_ok
                label_ok.config(image=label_ok.img)
                label_ok.grid(row=ii, column=jj)
            elif matriz[ii][jj] in viradas and [ii, jj] not in matriz_viradas:
                label_ok = Label(root, image='')
                pricture_ok = PhotoImage(file='logos/' + virada)
                label_ok.img = pricture_ok
                label_ok.config(image=label_ok.img)
                label_ok.grid(row=ii, column=jj)
            elif matriz[ii][jj] not in viradas:
                b = Button(root, image='')
                picture_d = PhotoImage(file='img_virada.png', name='pyimage' + str(idx))
                b.img = picture_d
                b.config(image=b.img)
                b.grid(row=ii, column=jj)
                b.bind('<Button-1>', on_click)
            idx += 1


def inicia():
    logos_files = os.listdir("logos")
    random_files = random.sample(logos_files, 6)
    random_files_2 = random_files
    joined_files = random_files_2 + random_files

    # criar tabela com imagens randómicas
    l = 0
    c = 0
    for l in range(3):
        linha = []
        for c in range(4):
            ran = secrets.choice(joined_files)
            joined_files.remove(ran)
            linha.append(ran)
            c += 1
        matriz.append(linha)
        l += 1

    # colocando as imagens da tabela no tela
    tot = 0
    gabarito_l = {}
    for i in range(3):
        for j in range(4):
            b = Label(root, image='')
            picture = PhotoImage(file='logos/' + matriz[i][j])
            gabarito_l[tot + 1] = matriz[i][j]
            gabarito.update(gabarito_l)
            b.img = picture
            b.config(image=b.img)
            b.grid(row=i, column=j)
            tot += 1

    mins.set('00')
    sec.set('05')
    lbl_mins = Entry(root, textvariable=mins, width=2)
    lbl_mins.grid(row=3, column=1)
    lbl_sec = Entry(root, textvariable=sec, width=2)
    lbl_sec.grid(row=3, column=2)
    root.after(5000, img_default, '')
    # contador de tempo para memorização
    times = int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        # Update tempo
        root.update()
        time.sleep(1)
        if times == 0:
            sec.set('00')
            mins.set('00')
        times -= 1
    mins.set('01')
    sec.set('00')
    # contador de tempo
    times = int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        # Update tempo
        root.update()
        time.sleep(1)
        if times == 0:
            sec.set('00')
            mins.set('00')
        times -= 1


Button(root, text='Começar', bd='2', bg='IndianRed1', font=('Helveticabold', 10), command=inicia).place(x=60, y=60)

root.mainloop()
