#!/usr/bin/python3
import tkinter as tk


class MyButton():
    def __init__(self, master,title,commandname,r,c,y):
        self.master = master
        self.button_result = None

        self.button = tk.Button(master, text=title, command=commandname)
        self.button.grid(row=r,column=c,pady=y)

    def button_action(self):
        self.button_result = "Data from button click!"
        print(f"Class attribute updated to: {self.button_result}")

