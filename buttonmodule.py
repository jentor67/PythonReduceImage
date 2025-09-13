#!/usr/bin/python3
import tkinter as tk


class MyButton():
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master) 

    def action(self, commandname):
        self.button.configure(command=commandname)

    def location(self, r, c, x, y):
        self.button.grid(row=r, column=c, padx=x, pady=y)

    def title(self,name_of_button):
        self.button.configure(text=name_of_button)



