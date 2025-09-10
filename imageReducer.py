#!/usr/bin/python3
import tkinter as tk
import os
from tkinter import filedialog

def pick_image_folder():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        input_label.config(text=f"Selected Folder:\n{selected_directory}")


        # Clear existing items in the Listbox
        file_listbox.delete(0, tk.END)

        try:
            files_and_dirs = os.listdir(selected_directory)
            for item in files_and_dirs:
                file_listbox.insert(tk.END, item)
        except OSError as e:
            file_listbox.insert(tk.END, f"Error: {e}")


def pick_converted_image_folder():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        output_label.config(text=f"Selected Folder:\n{selected_directory}")


# Create main window
root = tk.Tk()
root.title("Folder Picker")
root.geometry("800x400")

# Button to open folder dialog
btn_image = tk.Button(root, text="Image Folder", command=pick_image_folder)
btn_image.grid(row=0, column=0, pady=2)

# Label to display selected folder
input_label = tk.Label(root, text="No folder selected", wraplength=350, justify="center")
input_label.grid(row=1, column=0, pady=2)

# Button to open folder dialog
btn_converted_image = tk.Button(root, text="Image Folder", command=pick_converted_image_folder)
btn_converted_image.grid(row=2, column=0, pady=2)

# Label to display selected folder
output_label = tk.Label(root, text="No folder selected", wraplength=350, justify="center")
output_label.grid(row=3, column=0, pady=2)

file_listbox = tk.Listbox(root,width=60, height=15)
file_listbox.grid(row=0, column=2, columnspan=2, rowspan=4, padx= 2,  pady=2)

# Run the GUI
root.mainloop()

