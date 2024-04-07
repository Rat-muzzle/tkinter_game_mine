import mine_run
import time
import random
import tkinter as tk

from start_text import hello_text
from shop_run import def_shop
from mine_run import def_main
#from prison_run import def_prison
from tavern_run import def_tavern
from lumber_mill_run import def_lumber_mill
from start_loc_file import start_loc, def_killer

window = tk.Tk()
window.title('Поход  в шахту капать-капать')
window.geometry('400x400')
# переменные
gold = 0
hp = 10
pickaxe = None  # ='алмазна'   ='каменная'


start_loc(def_main, def_shop, def_tavern, def_lumber_mill)





# text_field = tk.Label(text='Приветствую вас в  деревне....', width=56, height=15, bg='yellow')
# text_field.grid(row=0)
# time.sleep(0)
text_field = tk.Label(text='Вы играете за персонажа....', width=56, height=15, bg='yellow')
text_field.grid(row=0)
time.sleep(0)

window.mainloop()
