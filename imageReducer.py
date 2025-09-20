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
import framemodule as fm
import tkinter as tk
import constants as ct
from tkinter import font
import os
from tkinter import filedialog
from tkcalendar import *
import datetime
from datetime import date


output_directory = ""
input_directory = ""


today = datetime.date.today()


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

    ConvertImage = reduceimagemodule.ImgReduce(
            input_directory,
            output_directory, 
            slider_quality.get(),
            slider_resolution.get())

    getItemParts = itemmodule.Item()

    files_and_dirs = os.listdir(input_directory)
    visible_items = [item for item in files_and_dirs if not item.startswith(".")]
    for item in visible_items: 
        print("Processing file: " + item)
        material, location, imagenumber, file_name, extension = \
          getItemParts.getparts(item)

        print("Material: " + material + " Location: " + location +
              " ImageNumber: " + imagenumber)

        present_date = cal.get_date()
        ConvertImage.process(
                item, file_name, present_date, extension)

    print("Done")


def update_label(value):
    # This function is called when the slider value changes
    slider_label.config(text=f"Quality Value: {int(float(value))}")

def update_res_label(value):
    # This function is called when the slider value changes
    slider_res_label.config(text=f"Resulution percentage Value: {int(float(value))}")


paddyX=15
paddyY=5


# Create main window
root = tk.Tk()
root.title("Image reducer")
root.geometry("1050x650")
root.configure(bg=ct.window_bg)


bold_font = font.Font(family="Arial", size=10, weight="bold")


## Choose the folder of the images  ##
# frame
image_frame = fm.MyFrame(root)
image_frame.location(1,0,2,paddyX,paddyY)

# title label
image_label = tk.Label(image_frame.frame,bg=ct.label_bg, 
                       text="Choose folder of images",font=bold_font)
image_label.pack(padx=10, pady=10)

# button
btn_image = buttonmodule.MyButton(image_frame.frame) 
btn_image.title("Image Folder")
btn_image.action(pick_image_folder)
btn_image.location_pack(paddyX,paddyY)

# folder display
input_label = tk.Label(image_frame.frame, bg=ct.label_bg,
     text="No folder selected", wraplength=350, justify="center")
input_label.pack(padx=10, pady=10)


## Choose the folder of the output images ##
# frame
image_out_frame = fm.MyFrame(root)
image_out_frame.location(3,0,2,paddyX,paddyY)

# title label
imageout_label = tk.Label(image_out_frame.frame, bg=ct.label_bg, 
    text="Choose folder of output",font=bold_font)
imageout_label.pack(padx=paddyX, pady=paddyY)

# button
btn_converted_image = buttonmodule.MyButton(image_out_frame.frame)
btn_converted_image.title("Output Imagee Folder")
btn_converted_image.action(pick_converted_image_folder)
btn_converted_image.location_pack(paddyX,paddyY)

# folder display
output_label = tk.Label(image_out_frame.frame, bg=ct.label_bg,
    text="No folder selected", wraplength=350, justify="center")
output_label.pack(padx=paddyX,  pady=paddyY)



## Choose image reduction
# frame
image_slider_frame = fm.MyFrame(root)
image_slider_frame.location(5,0,5,paddyX,paddyY)

# quality label 
quality_label = tk.Label(image_slider_frame.frame, bg=ct.label_bg,
    text="Quality",font=bold_font)
quality_label.pack(padx=paddyX, pady=paddyY)

# quality slider
slider_quality = tk.Scale(image_slider_frame.frame, from_=0, to=100, orient=tk.HORIZONTAL, 
     command=update_label,length=200, bg=ct.listbox_bg, troughcolor='green')
slider_quality.set(80)
slider_quality.pack( padx=paddyX, pady=paddyY)

# Create a label to display the quality's value
slider_label = tk.Label(image_slider_frame.frame, bg=ct.label_bg,
    text="Quality Value: 80")
slider_label.pack( padx=paddyX,  pady=paddyY)


# resolution label 
resolution_label = tk.Label(image_slider_frame.frame, bg=ct.label_bg,
    text="Resolution Percentage",font=bold_font)
resolution_label.pack(padx=paddyX, pady=paddyY)

# resolution slider
slider_resolution = tk.Scale(image_slider_frame.frame, from_=0, to=100, orient=tk.HORIZONTAL, 
     command=update_res_label,length=200, bg=ct.listbox_bg,troughcolor='blue')
slider_resolution.set(80)
slider_resolution.pack( padx=paddyX, pady=paddyY)

# Create a label to display the resolution percentage value
slider_res_label = tk.Label(image_slider_frame.frame, bg=ct.label_bg,
    text="Resulution percentage Value: 80")
slider_res_label.pack( padx=paddyX,  pady=paddyY)





# Create a label for list box
listbox_label = tk.Label(root, bg = ct.label_bg,
    text="Image list", font=bold_font)
listbox_label.grid(row=0, column=2, padx=paddyX, pady=paddyY, 
    sticky='W')


# list box of image files
file_listbox = tk.Listbox(root, bg=ct.listbox_bg, fg='black',
    width=40, height=25)
file_listbox.grid(row=1, column=2, columnspan=2, rowspan=10, 
    padx=paddyX,  pady=paddyY, sticky='W')


# Create a label for calendar
calendar_label = tk.Label(root, bg = ct.label_bg,
    text="Choose Date", font=bold_font)
calendar_label.grid(row=0, column=4, padx=paddyX, pady=paddyY, 
    sticky='W')


#### show calendar
cal = Calendar(root, selectmode="day", year=today.year, 
     month=today.month, day=today.day, date_pattern="yyyy-mm-dd")
cal.grid(row=1, column=4, rowspan=4, padx=paddyX, pady=paddyY, sticky='W')


# Button to Process Images
btn_process = buttonmodule.MyButton(root)
btn_process.title("Process Images")
btn_process.action(process_images)
btn_process.location(9, 4, paddyX, paddyY)

# Run the GUI
root.mainloop()

