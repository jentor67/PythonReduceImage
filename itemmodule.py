#!/usr/bin/python3
"""
File: itemmodule.py
Author: John Major
Date: 2025-09-15
Description:  Class to find the parse image file to determine
material, location, and image no
"""
import tkinter as tk

class Item():
    #def __init__(self):

    def getparts(self, item):
        fileparts = item.split('.')
        filedescription = fileparts[0].split('_')
        material = filedescription[0]
        location = filedescription[1]
        imagenumber = filedescription[2]

        return material, location, imagenumber





