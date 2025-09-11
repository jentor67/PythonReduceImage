#!/usr/bin/python3
import reduceimagemodule
import buttonmodule
import tkinter as tk
import os
from tkinter import filedialog


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
    print("Hello")
    print(output_directory)

# Create main window
root = tk.Tk()
root.title("Folder Picker")
root.geometry("800x400")

# Button to open folder dialog
btn_image = buttonmodule.MyButton(root,"Image Folder", "pick_image_folder",0,0,2)

# Label to display selected folder
input_label = tk.Label(root, text="No folder selected", 
                       wraplength=350, justify="center")
input_label.grid(row=1, column=0, pady=2)

# Button to open folder dialog
btn_converted_image = buttonmodule.MyButton(root,"Output Image Folder", 
                                            "pick_converted_image_folder",2,0,2)

# Label to display selected folder
output_label = tk.Label(root, text="No folder selected", wraplength=350, justify="center")
output_label.grid(row=3, column=0, pady=2)

# Button to open folder dialog
btn_process = tk.Button(root, text="Process Images", command=process_images)
btn_process.grid(row=4, column=0, pady=2)

file_listbox = tk.Listbox(root,width=60, height=15)
file_listbox.grid(row=0, column=2, columnspan=2, rowspan=4, padx= 2,  pady=2)

#bbtn_test = buttonmodule.MyButton(root,5,0,2)

# Run the GUI
root.mainloop()

