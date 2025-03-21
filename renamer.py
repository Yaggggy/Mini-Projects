import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def rename_files():
    folder = folder_path.get()
    prefix = prefix_entry.get().strip()

    if not folder:
        messagebox.showerror("Error", "Please select a folder!")
        return
    
    if not prefix:
        messagebox.showerror("Error", "Please enter a prefix!")
        return
    
    try:
        files = os.listdir(folder)
        count = 1

        for file in files:
            file_path = os.path.join(folder, file)

            if os.path.isfile(file_path):  
                extension = os.path.splitext(file)[1]
                new_name = f"{prefix}_{count}{extension}"
                new_path = os.path.join(folder, new_name)
                os.rename(file_path, new_path)
                count += 1

        messagebox.showinfo("Success", "Files renamed successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Bulk File Renamer")
root.geometry("400x250")

folder_path = tk.StringVar()

tk.Label(root, text="Select Folder:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=40).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

tk.Label(root, text="Enter Prefix:").pack(pady=5)
prefix_entry = tk.Entry(root, width=30)
prefix_entry.pack()

tk.Button(root, text="Rename Files", command=rename_files).pack(pady=20)

root.mainloop()
