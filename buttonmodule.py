#!/usr/bin/python3
"""
File: buttonmodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to create button
"""
import tkinter as tk
import constants as ct

#tk.Button(root, text="Click Me", width=15, height=1)

class MyButton():
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master)
        self.button.configure(
                width=15, 
                height=1,
                bg=ct.button_bg)

    def action(self, commandname):
        self.button.configure(command=commandname)

    def location(self, r, c, x, y):
        self.button.grid(row=r, column=c, padx=x, pady=y)

    def location_pack(self, x, y):
        self.button.pack(padx=x, pady=y)

    def title(self,name_of_button):
        self.button.configure(text=name_of_button)



