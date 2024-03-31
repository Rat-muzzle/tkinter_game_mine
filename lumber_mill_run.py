import tkinter as tk
import tkinter as tk
from start_loc_file import start_loc, def_killer


def def_lumber_mill(event):
    def_killer()
    text_field = tk.Label(text='вы славно порубили дерево пора возврааться домой', width=56, height=15, bg='yellow')
    text_field.grid(row=0)

    # button_lumber_end = tk.Button(text='домой', bg='pink', command=lambda: [def_killer(), start_loc])
    # button_lumber_end.grid(column=0, row=1)
    # button_lumber_end.bind("<Button-1>", start_loc)
