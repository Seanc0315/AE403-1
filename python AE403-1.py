# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:58:28 2020

@author: admin
"""


import tkinter as tk

def clickMe():
    tk.messagebox.showinfo(title = '提示', message = '好痛')

window = tk.Tk()

window.title("我的第一個GUI程式")

window.geometry('300x300')

label = tk.Label(window, text = "我的GUI", bg = '#00BBFF', fg = '#000000')
label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()

button = tk.Button(window, text = "Enter", command = clickMe)
button.pack()


window.mainloop()