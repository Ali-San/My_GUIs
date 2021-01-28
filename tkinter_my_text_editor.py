"""
I started writing this program during my 100 days of code challenge,
I haven't been able to finish it yet, but I will get it done one day!
Jan 28, 2021.
"""

import tkinter as tk
from tkinter import ttk

class TextEditor():
    def __init__(self, master):
        self.master = master
        master.title("☆ I'm a Text Editor! ☆")
        # create frm
        self.frm = tk.Frame(master)
        
        # create the menubar
        menubar = tk.Menu(master)
        
        # build 'File' menu
        menu_file = tk.Menu(menubar, tearoff=0)
        
        menu_file.add_command(label='New', command=self.donothing)
        menu_file.add_command(label='Open', command=self.donothing)
        menu_file.add_command(label='Close', command=self.donothing)
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.master.destroy)
        
        menubar.add_cascade(menu=menu_file, label='File')
        
        # build 'Edit' menu
        menu_edit = tk.Menu(menubar, tearoff=0)
        menu_edit.add_command(label='Cut', command=self.donothing)
        menu_edit.add_command(label='Copy', command=self.donothing)
        menu_edit.add_command(label='Paste', command=self.donothing)
        menubar.add_cascade(menu=menu_edit, label='Edit')
        
        # build 'Search' menu
        menu_search = tk.Menu(menubar, tearoff=0)
        menu_search.add_command(label='Find', command=self.search_window)
        menu_search.add_command(label='Mark', command=self.mark_window)
        menubar.add_cascade(menu=menu_search, label='Search')
        
        # build 'About' menu
        menu_about = tk.Menu(menubar, tearoff=0)
        menu_about.add_command(label='About this program', command=self.about_message)
        menubar.add_cascade(menu=menu_about, label='About...')
        
        # display the menubar
        self.master.config(menu=menubar)
        
        # build textbox
        self.text_box = tk.Text(self.frm, height=800, width=800)
        # add numbers to lines in text?
        # https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget

        # build textbox scrollbar
        # http://effbot.org/zone/tkinter-scrollbar-patterns.htm
        
        # LAYOUT
        self.frm.pack()
        self.text_box.pack()
        
    # METHODS
    def donothing(self):
        pass

    # create Search window:
    def search_window(self):
        top = tk.Toplevel()
        top.title('Search...')
        lbl = tk.Label(top, text='Enter text: ')
        ent = tk.Entry(top, width=20)
        btn = tk.Button(top, text='Find', relief=tk.RAISED, bd=3, command=self.find_text)
        lbl.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT)
        btn.pack(side=tk.LEFT)
        
    # ADD OPTIONS WITH REGEX
    
    # create Mark window:
    def mark_window(self):
        top = tk.Toplevel()
        top.title('Mark all...')
        msg = tk.Message(top, text='Enter the word(s) you would like to highlight, choose a color and press the "Mark" button.', aspect=500)
        lbl = tk.Label(top, text='Word(s):')
        ent = tk.Entry(top, width=20)
        msg.pack(fill=tk.BOTH, expand=1)
        lbl.pack(side=tk.LEFT, padx=5)
        ent.pack(side=tk.LEFT)
        
        # give different color options:
        colors = [('Blue', 'blue'),
                ('Green', 'green'),
                ('Yellow', 'yellow'),
                ('Pink', 'pink')
                ]
        color = tk.StringVar()
        
        for text, value in colors:
            text_color = ttk.Radiobutton(top, text=text, variable=color, value=value, command=self.donothing)
            text_color.pack(anchor=tk.W)
        
        btn_mark = tk.Button(top, text='Mark', relief=tk.RAISED, bd=3, state=tk.DISABLED, command=self.mark_text)
        btn_mark.pack(padx=10, pady=10)
    
    def about_message(self):
        top = tk.Toplevel()
        top.title('About this program...')
        text='I am writing this program as a challenge to myself, it is my first "big" GUI and it will take some time to finish it because I still don\'t know how to code everything that I want to include in it. Hopefully it will be ready by summertime. Today is Feb 20, 2020. Let\'s see what I can do B-)\nAfter the pandemic started, it was almost impossible to continue, so I left this program behind and focused only on learning data science, but I still want to finish it, and I will eventually. Today is Jan 28, 2021. Let\'s see when I can finally say "It\'s done!".'
        msg = tk.Message(top, text=text, aspect=400)
        msg.pack()

    def mark_text(self):
        '''Idea: when the user chooses one color option from the radiobuttons, btn_mark state changes to NORMAL, and when pressed all occurrences of the text entered in ent are highlighted'''
        pass
        
    def find_text(self):
        '''Idea: get text from entry and find it in the textbox, if found, highlight it, else show message 'Text not found'
        '''
        pass

root = tk.Tk()
app = TextEditor(root)
root.mainloop()