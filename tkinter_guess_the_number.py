'''
from my 100 days of code challenge:
    
The exercise was taken from:
https://python-textbok.readthedocs.io/en/latest/Introduction_to_GUI_Programming.html
and
https://python-textbok.readthedocs.io/en/latest/Useful_Libraries.html

Write a program which randomly picks an integer from 1 to 100. Your program should prompt the user for guesses – if the user guesses incorrectly, it should print whether the guess is too high or too low. If the user guesses correctly, the program should print how many guesses the user took to guess the right answer. You can assume that the user will enter valid input.
'''

import tkinter as tk
import random

secret_n = random.randint(1, 100)

class GuessNumber():
    def __init__(self, master):
        
        self.master = master
        master.title("Guess a Number - a simple game")
        
        # build upper_frm for labels
        self.upper_frm = tk.Frame(master, bg='#66CDAA')
        
        # welcome_lbl welcomes + explain game
        self.welcome_lbl = tk.Label(self.upper_frm, text="Welcome to Guess a Number!\nI'm thinking about a positive integer\nbetween 1 and 100,\ncan you guess which one?", bg='#66CDAA')
        
        # build lower_frm for ent + btn
        self.lower_frm = tk.Frame(master, bg='#FFFFF0')
        
        # update_lbl shows how the game is developing
        self.update_lbl = tk.Label(self.lower_frm, text='Go ahead, you can press "Guess" now', bg='#FFFFF0')
        
        # entry width=20 IntVar()
        #self.ent_var = tk.IntVar()
        vcmd = master.register(self.validate) # we have to wrap the command
        self.ent = tk.Entry(self.lower_frm, width=10, validate='key', validatecommand=(vcmd, '%P'))
        
        # btn_guess
        self.btn_guess = tk.Button(self.lower_frm, text='Guess', bg='#59B395', relief=tk.RAISED, bd=3, command=self.choose)
        
        # btn_reset
        self.btn_reset = tk.Button(self.lower_frm, text='Reset', bg='#59B395', relief=tk.RAISED, bd=3, command=self.reset)
        
        # btn_quit
        self.btn_quit = tk.Button(self.lower_frm, text='Quit', command=self.master.destroy, bg='#59B395', relief=tk.RAISED, bd=3)
        
        # build side_frm for score keeping
        self.side_frm = tk.Frame(master, bg='#CD6689')
        self.lbl_side = tk.Label(self.side_frm, bg='#CD6689', text='Guess count:')
        self.lbl_count = tk.Label(self.side_frm, bg='#CD6689', text='0')
        self.lbl_nums = tk.Label(self.side_frm, bg='#CD6689', text='')
        
        # LAYOUT
        # root
        master.rowconfigure([0, 1, 2, 3], minsize=100)
        master.columnconfigure([0, 1, 2, 3], minsize=100)
        master.resizable(False, False)
        
        # upper_frm
        self.upper_frm.grid(row=0,column=0, columnspan=3, sticky='nsew')
        self.welcome_lbl.grid(row=0, columnspan=3, sticky='ew', ipadx=50, pady=30)
        
        # lower_frm
        self.lower_frm.grid(row=1, column=0, rowspan=3, columnspan=3, sticky='nsew')
        self.lower_frm.rowconfigure([0, 1, 2, 3], minsize=75)
        self.lower_frm.columnconfigure([0, 1, 2], minsize=75)
        self.update_lbl.grid(row=0, column=1, sticky='ew', pady=20)
        self.ent.grid(row=1, column=1, padx=10, pady=10)
        self.btn_guess.grid(row=2, column=1, padx=10, pady=10)
        self.btn_reset.grid(row=3, column=1, padx=10, pady=30, sticky='e')
        self.btn_quit.grid(row=3, column=2, padx=10, pady=30, sticky='w')
        
        # side_frm
        self.side_frm.grid(row=0, rowspan=4, column=3, sticky='nsew')
        self.lbl_side.grid(row=0, ipadx=10, padx=10, pady=10, sticky='nsew')
        self.lbl_count.grid(row=1, padx=10, sticky='nsew')
        self.lbl_nums.grid(row=2, padx=10, sticky='nsew')
        
        # methods:
    def choose(self):
        '''Evaluate the user's guess and display the result through self.update_lbl and self.lbl_count.
        '''
        user_guess = int(self.ent.get())
        old_value = self.lbl_count['text']
        old_num = self.lbl_nums['text']
        
        if user_guess == secret_n:
            new_value = str(int(old_value) + 1)
            self.lbl_count['text'] = new_value
            self.update_lbl['text'] = 'Congratulations!!!\nYou guessed my number after {} tries'.format(self.lbl_count['text'])
            new_num = self.ent.get()
            self.lbl_nums['text'] = old_num + '\n' + new_num
        elif user_guess < secret_n:
            self.update_lbl['text'] = "Too low!"
            new_value = str(int(old_value) + 1)
            self.lbl_count['text'] = new_value
            new_num = self.ent.get()
            self.lbl_nums['text'] = old_num + '\n' + new_num
        elif user_guess > secret_n:
            self.update_lbl['text'] = "Too high!"
            new_value = str(int(old_value) + 1)
            self.lbl_count['text'] = new_value
            new_num = self.ent.get()
            self.lbl_nums['text'] = old_num + '\n' + new_num
        
    def reset(self):
        self.ent.delete(0, tk.END)
        self.update_lbl['text'] = 'Go ahead, you can press "Guess" now'
        self.lbl_count['text'] = '0'
        self.lbl_nums['text'] = ''
    
    def validate(self, new_text):
        if not new_text:
            # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    
root = tk.Tk()
my_game = GuessNumber(root)
root.mainloop()