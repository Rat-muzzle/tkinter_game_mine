import tkinter as tk
from start_loc_file import start_loc, def_killer

hp = 10
many = 15

def def_pivo(event):
    text_field = tk.Label(text='ты выпил пиво и все круто', width=56, height=15, bg='yellow')
    hp += 1
    many -= 3

def def_hleb(event):
    text_field = tk.Label(text='ты cъел хлеб и все круто', width=56, height=15, bg='yellow')
    hp += 4
    many -= 5

def def_aple(event):
    text_field = tk.Label(text='ты cъел хлеб и все круто', width=56, height=15, bg='yellow')
    hp += 2
    many -= 4


def def_tavern(event):
    def_killer()
    text_field = tk.Label(text='Добро пожаловать в таверну', width=56, height=15, bg='yellow')
    text_field.grid(row=5)
    def_killer()
    global button1, button2, button3, button4
    button1 = tk.Button(text='пиво', bg='green')
    button1.grid(column=0, row=1)
    button1.bind("<Button-1>", def_pivo)

    button2 = tk.Button(text='хлеб', bg='green')
    button2.grid(column=0, row=1)
    button2.bind("<Button-1>", def_hleb)

    button1 = tk.Button(text='яблоко', bg='green')
    button1.grid(column=0, row=1)
    button1.bind("<Button-1>", def_tavern)

