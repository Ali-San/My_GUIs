"""
from my 100 days of code challenge:

This program is a "pythonic" die you can roll. 
"""

import tkinter as tk
import random

# roll the die (and update the label, which is the whole point of the exercise)
def roll_the_die():
    result = random.randint(1, 6)
    lbl_result['text'] = result

root = tk.Tk()
root.title("Roll the die! Good luck!")
frm = tk.Frame(root)
frm.pack()

frm.rowconfigure([0, 1], minsize=40, weight=1)
frm.columnconfigure(0, minsize=120, weight=1)

btn_die = tk.Button(frm, text="Roll", fg='white', bg='#8B008B', command=roll_the_die)
btn_die.grid(row=0, column=0, sticky='nsew')

lbl_result = tk.Label(frm, text='')
lbl_result.grid(row=1, column=0, sticky='nsew')

root.mainloop()