"""
Author: Coralys Colon Vargas
Date written: 02/26/2025  
Assignment: Final Project - Task Manager (Initial Setup)
Short Desc: Basic GUI structure for the Task Manager application.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def open_add_task_window():
    """Opens the Add/Edit Task window."""
    add_edit_window = tk.Toplevel(main_window)
    add_edit_window.title("Add Task")
    create_add_edit_window_elements(add_edit_window)

def create_add_edit_window_elements(window):
    """Creates the elements for the Add/Edit Task window."""
    tk.Label(window, text="Task Description:").grid(row=0, column=0, sticky="w")
    tk.Entry(window).grid(row=0, column=1)

    tk.Label(window, text="Category:").grid(row=1, column=0, sticky="w")
    ttk.Combobox(window, values=["Work", "Personal", "Errands"]).grid(row=1, column=1)

    tk.Label(window, text="Priority:").grid(row=2, column=0, sticky="w")
    ttk.Combobox(window, values=["High", "Medium", "Low"]).grid(row=2, column=1)

    tk.Label(window, text="Due Date:").grid(row=3, column=0, sticky="w")
    # Add date entry widget here later

    tk.Button(window, text="Save").grid(row=4, column=0)
    tk.Button(window, text="Cancel", command=window.destroy).grid(row=4, column=1)

def exit_application():
    """Exits the application."""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        main_window.destroy()

# Main Window
main_window = tk.Tk()
main_window.title("Task Manager")

# Labels
tk.Label(main_window, text="Task Manager").pack(pady=10)

# Buttons
tk.Button(main_window, text="Add Task", command=open_add_task_window).pack(pady=5)
tk.Button(main_window, text="Edit Task").pack(pady=5)
tk.Button(main_window, text="Delete Task").pack(pady=5)
tk.Button(main_window, text="Filter").pack(pady=5)
tk.Button(main_window, text="Sort").pack(pady=5)
tk.Button(main_window, text="Exit", command=exit_application).pack(pady=5)

# Treeview (Placeholder)
tree = ttk.Treeview(main_window)
tree.pack(pady=10)

# Image (Placeholder - add actual image later)
tk.Label(main_window, text="Image Placeholder").pack()

main_window.mainloop()