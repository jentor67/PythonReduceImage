#!/usr/bin/python3
"""
File: imageReducer.py
Author: John Major
Date: 2025-09-14
Description:  This program lets the user choose a folder with images, 
folder for the output, and a slider between 0-100 to choose the 
reduce image using Pillow

associated file:
    buttonmodule.py
    reduceimagemodule.py
"""

import reduceimagemodule
import buttonmodule
import itemmodule
import tkinter as tk
import os
from tkinter import filedialog
#from tkcalendar import Calendar


output_directory = ""
input_directory = ""

def pick_image_folder():
    global input_directory
    input_directory = filedialog.askdirectory()
    if input_directory:
        input_label.config(text=f"Selected Folder:\n{input_directory}")


        # Clear existing items in the Listbox
        file_listbox.delete(0, tk.END)

        try:
            image_files = []
            files_and_dirs = os.listdir(input_directory)
            for item in files_and_dirs:
                image_files.append(item)
                file_listbox.insert(tk.END, item)
        except OSError as e:
            file_listbox.insert(tk.END, f"Error: {e}")
     
    return image_files


def pick_converted_image_folder():
    global output_directory
    output_directory = filedialog.askdirectory()
    if output_directory:
        output_label.config(text=f"Selected Folder:\n{output_directory}")


def process_images():

    ConvertImage = reduceimagemodule.ImgReduce(input_directory,
        output_directory, slider.get())

    getItemParts = itemmodule.Item()

    files_and_dirs = os.listdir(input_directory)
    visible_items = [item for item in files_and_dirs if not item.startswith(".")]
    for item in visible_items: 
        print("Processing file: " + item)
        material, location, imagenumber = getItemParts.getparts(item)

        print("Material: " + material + " Location: " + location +
              " ImageNumber: " + imagenumber)
        ConvertImage.process(item)

    print("Done")


def update_label(value):
    # This function is called when the slider value changes
    slider_label.config(text=f"Slider Value: {int(float(value))}")


paddyX=5
paddyY=5


# Create main window
root = tk.Tk()
root.title("Image reducer")
root.geometry("800x400")


# Button to choose folder the images are at
btn_image = buttonmodule.MyButton(root) 
btn_image.title("Image Folder")
btn_image.action(pick_image_folder)
btn_image.location(0,0,paddyX,paddyY)


# Label to display selected folder
input_label = tk.Label(root, text="No folder selected", 
     wraplength=350, justify="center")
input_label.grid(row=1, column=0, padx=paddyX, pady=paddyY)


# Button to choose converted folder
btn_converted_image = buttonmodule.MyButton(root)
btn_converted_image.title("Output Imagee Folder")
btn_converted_image.action(pick_converted_image_folder)
btn_converted_image.location(2,0,paddyX,paddyY)


# Label to display selected folder
output_label = tk.Label(root, text="No folder selected", 
    wraplength=350, justify="center")
output_label.grid(row=3, column=0, padx=paddyX,  pady=paddyY)


# Create a label for Slider
reducer_label = tk.Label(root, text="Percentage reducer")
reducer_label.grid(row=4, column=0, padx=paddyX, pady=paddyY)


# Create a horizontal slider
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, 
     command=update_label)
slider.grid(row=5, column=0, padx=paddyX, pady=paddyY)


# Create a label to display the slider's value
slider_label = tk.Label(root, text="Slider Value: 0")
slider_label.grid(row=6, column=0, padx=paddyX,  pady=paddyY)


# Button to Process Images
btn_process = buttonmodule.MyButton(root)
btn_process.title("Process Images")
btn_process.action(process_images)
btn_process.location(6, 0, paddyX, paddyY)


# Create a label for list box
listbox_label = tk.Label(root, text="Image list")
listbox_label.grid(row=0, column=2, padx=20, pady=paddyY, 
    sticky='W')


# list box of image files
file_listbox = tk.Listbox(root, width=60, height=15)
file_listbox.grid(row=1, column=2, columnspan=2, rowspan=6, 
    padx= 20,  pady=paddyY, sticky='W')


# Run the GUI
root.mainloop()

