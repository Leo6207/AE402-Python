# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:36:45 2024

@author: hungy
"""

import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.title("My fisrt GUI APP")

window.geometry('300x300')

label = tk.Label(window, text ="味全龍", bg='#F00', fg='#000')
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

def clickme():
    tkinter.messagebox.showinfo(title="提示", message="龍眾一心")
    
button = tk.Button(window, text="送出", command=clickme)
button.pack()

window.mainloop()

 