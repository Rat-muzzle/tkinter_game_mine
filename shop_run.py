import tkinter as tk

import main
from start_loc_file import start_loc, def_killer
hp = main.hp
gold = main.gold
def def_lottery(event):
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    text_field1 = tk.Label(text='Ты купил билет, ты проиграл', width=56, height=15, bg='yellow')
    text_field1.grid(row=0)
gold -= 2
def def_xleb(event):
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    text_field2 = tk.Label(text='Ты купил хлеб, ты покушал', width=56, height=15, bg='yellow')
    text_field2.grid(row=0)
hp += 1
gold -= 1

def def_maclo(event):
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    text_field3 = tk.Label(text='Ты намазал на хлеб масло, ты стал жертресом', width=56, height=15, bg='yellow')
    text_field3.grid(row=0)
hp += 3
gold -= 2
def def_shop(event):
    def_killer()
    text_field = tk.Label(text='Вы пришли в магазин, что ты купишь?', width=56, height=15, bg='blue')
    text_field.grid(row=0)

    global button1, button2, button3
    button1 = tk.Button(text='Лотерея', bg='red')
    button1.grid(column=0, row=1)
    button1.bind("<Button-1>", def_lottery)

    button2 = tk.Button(text='Хлеб', bg='red')
    button2.grid(column=0, row=2)
    button2.bind("<Button-1>", def_xleb)

    button3 = tk.Button(text='Масло', bg='red')
    button3.grid(column=0, row=3)
    button3.bind("<Button-1>", def_maclo)

