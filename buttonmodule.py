#!/usr/bin/python3
"""
File: buttonmodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to create button
"""
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



