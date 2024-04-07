import tkinter as tk
import time
import random
from start_loc_file import def_killer
from start_loc_file import hp, gold
def def_main(event):
    def_killer()
    button1 = tk.Button(text='работать в шахте', bg='pink')
    button1.grid(column=0, row=1)
    button1.bind("<Button-1>", def_work)

    button2 = tk.Button(text='отдыхать', bg='pink')
    button2.grid(column=0, row=2)
    button2.bind("<Button-1>", def_chill_out)

def def_work(event):
    global hp, gold
    hp -= 7
    gold += 10
    text_field = tk.Label(text='Вы работали в шахте и заработали денег. +10 gold, -7 hp', width=56, height=15, bg='yellow')
    text_field.grid(row=0)

def def_chill_out(event):
    global hp
    hp += 5
    text_field = tk.Label(text='Вы решили отдохнуть, но ничего не заработали. +5 hp', width=56, height=15,
                          bg='yellow')
    text_field.grid(row=0)
    time.sleep(1)
    random_fight = random.randint(1,3)
    if random_fight == 1:
        hp -= 7
        text_field_2 = tk.Label(text = 'Рабочие побили вас за преждевременный отдых, -7 hp', width=56, height=15,
                          bg='yellow')
        text_field_2.grid(row=1)