from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def no():
    messagebox.showinfo('', 'todo errado você')
    quit()

def motionMouse(event):
    ButtonYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)  # Correção: "heigh" para "height"
root.configure(bg='white')  # Correção: Substituição de ',' por '='

label = Label(root, text='você Aceita Namorar Comigo?', font='Arial 20 bold', bg='white')
label.pack()  # O método pack() deve ser chamado em uma linha separada
ButtonYes = Button(root, text='Não', font='Sim')
ButtonYes.place(x=170, y=100)
ButtonYes.bind('<Enter>', motionMouse)
ButtonNo = Button(root, text='Sim', font='Arial 20 bold', command=no)
ButtonNo.place(x=350, y=100)  # Movido a vírgula para antes do "command"

root.mainloop()