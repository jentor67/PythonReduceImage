#!/usr/bin/python3
"""
File: itemmodule.py
Author: John Major
Date: 2025-09-15
Description:  Class to find the parse image file to determine
segment1, segment2, and segment3
"""
import tkinter as tk

class Item():
    #def __init__(self):

    def getparts(self, item):
        fileparts = item.split('.')
        filedescription = fileparts[0].split('_')
        seg1 = filedescription[0]
        seg2 = filedescription[1]
        seg3 = filedescription[2]

        return filedescription, fileparts[0], fileparts[1]





