#!/usr/bin/python3
"""
File: framemodule.py
Author: John Major
Date: 2025-09-14
Description:  Class to create frame
"""
import tkinter as tk
import constants as ct


class MyFrame():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(
                master, 
                width=250, 
                height=100, 
                bg=ct.midnight_green,
                relief="solid", 
                borderwidth=1)

    def location(self, r, c, rs, x, y):
        self.frame.grid(row=r, column=c, rowspan= rs, padx=x, pady=y)

    def location_pack(self, x, y):
        self.frame.pack(padx=x, pady=y)


