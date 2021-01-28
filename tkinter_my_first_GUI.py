"""
A program from my 100 days of code challenge.

"""

import tkinter

red_button_msg = "Welcome to the Matrix"
green_button_msg = "Have a nice day!"

def message(msg):
    top = tkinter.Toplevel()
    top.title(';)')
    label = tkinter.Label(top, text=msg)
    label.pack()

window = tkinter.Tk()
window.title("My first GUI")

label = tkinter.Label(window, text="Hello GUI's World!")
label.pack()

button_red = tkinter.Button(window, text="I'm a red button!", fg='white', bg='red', command=lambda: message(red_button_msg))
button_red.pack(side='left')

button_green = tkinter.Button(window, text="I'm a green button!", fg='white', bg='green', command=lambda: message(green_button_msg))
button_green.pack(side='right')

window.mainloop()