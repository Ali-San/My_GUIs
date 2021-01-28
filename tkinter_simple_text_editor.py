"""
from my 100 days of code challenge:
    
I wrote this text editor following this tutorial (with a few extras I made up):

https://realpython.com/python-gui-tkinter/#building-a-text-editor-example-app
"""

import tkinter as tk
import tkinter.filedialog as fd
# another way of importing this:
# from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = fd.askopenfilename(
    filetypes = [('Text files', '*.txt'), ('All files', '*.*')]
    )
    if not filepath:
        return
    txt_edit.delete('1.0', tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f'Simple Text Editor - {filepath}')

def save_file():
    """Save the current file as a new file."""
    filepath = fd.asksaveasfilename(
        defaultextension="txt",
        filetypes=[('Text files', '*.txt'),('All files', '*.*')],
        )
    # the next 2 lines check to see if the user closes the dialog box or clicks the Cancel button. If so, then filepath will be None, and the function will return without executing any of the code to save the text to a file.
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get('1.0', tk.END)
        output_file.write(text)
    root.title(f'Simple Text Editor - {filepath}')


root = tk.Tk()
root.title('Simple Text Editor')
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)
root.configure(bg='steelblue')

frm_buttons = tk.Frame(root, relief=tk.GROOVE, bd=3, bg='steelblue')#, height=800, width=100)
frm_buttons.grid(row=0, column=0,sticky='ns')

btn_open = tk.Button(frm_buttons, text="Open", relief=tk.RAISED, bd=2, fg='#F0FFFF', bg='#3D729E', command=open_file)
btn_open.grid(row=0, column=0, padx=7, pady=7, sticky='ew')

btn_save = tk.Button(frm_buttons, text="Save as...", relief=tk.RAISED, bd=2, fg='#F0FFFF', bg='#3D729E', command=save_file)
btn_save.grid(row=1, column=0, padx=7, sticky='ew')

btn_quit = tk.Button(frm_buttons, text="Quit", relief=tk.RAISED, bd=2, fg='#F0FFFF', bg='#3D729E', command=root.destroy)
btn_quit.grid(row=2, column=0, padx=7, pady=780, sticky='ew')

txt_edit = tk.Text(root, height=800, width=800)
txt_edit.grid(row=0, column=1, sticky='nsew')

root.mainloop()