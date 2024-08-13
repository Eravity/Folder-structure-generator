import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
import pyperclip

# Colors
colors = {
    "background": "#cad2c5",
    "button_bg": "#84a98c",
    "button_fg": "#ffffff",
    "text_bg": "#52796f",
    "text_fg": "#cad2c5",
    "border": "#354f52"
}

def print_directory_structure(root_dir, text_widget, indent_level=0):
    try:
        directories = []
        files = []
        for item in os.listdir(root_dir):
            if item == "node_modules":
                continue
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                directories.append(item)
            else:
                files.append(item)

        for directory in directories:
            dir_path = os.path.join(root_dir, directory)
            text_widget.insert(tk.END, ' ' * indent_level * 4 + '|-- ' + directory + '\n')
            print_directory_structure(dir_path, text_widget, indent_level + 1)

        for file in files:
            file_path = os.path.join(root_dir, file)
            text_widget.insert(tk.END, ' ' * indent_level * 4 + '|-- ' + file + '\n')

    except PermissionError:
        text_widget.insert(tk.END, ' ' * indent_level * 4 + '|-- [Permission Denied]\n')

def select_folder():
    folder_path = filedialog.askdirectory(title="Selectați folderul principal")
    if folder_path:
        text_widget.delete(1.0, tk.END) 
        text_widget.insert(tk.END, "Structura folderului principal:\n")
        print_directory_structure(folder_path, text_widget)
    else:
        text_widget.delete(1.0, tk.END)  
        text_widget.insert(tk.END, "Nu a fost selectat niciun folder.\n")

def copy_to_clipboard():
    content = text_widget.get(1.0, tk.END)
    pyperclip.copy(content)
    copy_button.config(text="Copied!")

root = tk.Tk()
root.title("Vizualizator Structură Folder")
root.geometry("800x600")
root.configure(bg=colors["background"])


root.tk.call('tk', 'scaling', 1.5)

label = tk.Label(root, text="Selectați un folder pentru a vedea structura acestuia:", font=("Arial", 12), bg=colors["background"], fg=colors["text_fg"])
label.pack(pady=(10, 5))  

select_button = tk.Button(root, text="Selectează Folder", command=select_folder, font=("Arial", 12), bg=colors["button_bg"], fg=colors["button_fg"], relief=tk.RAISED, bd=2, padx=10, pady=5)
select_button.pack(pady=5)

copy_button = tk.Button(root, text="Copiază Structura", command=copy_to_clipboard, font=("Arial", 12), bg=colors["button_bg"], fg=colors["button_fg"], relief=tk.RAISED, bd=2, padx=10, pady=5)
copy_button.pack(pady=5)

text_widget = scrolledtext.ScrolledText(root, width=100, height=30, font=("Courier New", 10), bg=colors["text_bg"], fg=colors["text_fg"], borderwidth=2, relief="sunken")
text_widget.pack(pady=(10, 5), fill=tk.BOTH, expand=True)  # Marginile de sus și jos sunt diferite pentru widgetul de text

root.mainloop()
