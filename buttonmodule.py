#!/usr/bin/python3
"""
File: buttonmodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to create button
"""
import tkinter as tk
import constants as ct


class MyButton():
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master)
        self.button.configure(
                   activebackground=ct.button_active,
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg=ct.button_bg,
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 11),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100
                )

    def action(self, commandname):
        self.button.configure(command=commandname)

    def location(self, r, c, x, y):
        self.button.grid(row=r, column=c, padx=x, pady=y)

    def location_pack(self, x, y):
        self.button.pack(padx=x, pady=y)

    def title(self,name_of_button):
        self.button.configure(text=name_of_button)



