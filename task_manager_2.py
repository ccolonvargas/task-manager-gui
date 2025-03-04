"""
Author: Coralys Colon Vargas
Date written: 03/01/2025
Assignment: Final Project - Task Manager (Continuation)
Short Desc: Basic GUI structure for the Task Manager application.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

def open_add_task_window(task_to_edit=None):
    """Opens the Add/Edit Task window.
    
    Args:
        task_to_edit: If provided, the task data to edit.
    """
    if task_to_edit:
        add_edit_window = tk.Toplevel(main_window)
        add_edit_window.title("Edit Task")
        create_add_edit_window_elements(add_edit_window, task_to_edit)
    else:
        add_edit_window = tk.Toplevel(main_window)
        add_edit_window.title("Add Task")
        create_add_edit_window_elements(add_edit_window)

def create_add_edit_window_elements(window, task_to_edit=None):
    """Creates the elements for the Add/Edit Task window.
    
    Args:
        window: The Toplevel window to add elements to.
        task_to_edit: If provided, the task data to pre-fill the form.
    """
    tk.Label(window, text="Task Description:").grid(row=0, column=0, sticky="w")
    description_entry = tk.Entry(window)
    description_entry.grid(row=0, column=1)

    tk.Label(window, text="Category:").grid(row=1, column=0, sticky="w")
    category_combobox = ttk.Combobox(window, values=["Work", "Personal", "Errands"])
    category_combobox.grid(row=1, column=1)

    tk.Label(window, text="Priority:").grid(row=2, column=0, sticky="w")
    priority_combobox = ttk.Combobox(window, values=["High", "Medium", "Low"])
    priority_combobox.grid(row=2, column=1)

    tk.Label(window, text="Due Date:").grid(row=3, column=0, sticky="w")
    due_date_entry = tk.Entry(window)
    due_date_entry.grid(row=3, column=1)

    if task_to_edit:
        description_entry.insert(0, task_to_edit["description"])
        category_combobox.set(task_to_edit["category"])
        priority_combobox.set(task_to_edit["priority"])
        due_date_entry.insert(0, task_to_edit["due_date"])

    def save_task():
        description = description_entry.get()
        category = category_combobox.get()
        priority = priority_combobox.get()
        due_date = due_date_entry.get()

        # Basic validation (add more robust validation)
        if not description or not category or not priority or not due_date:
            messagebox.showerror("Error", "All fields are required.")
            return

        # Attempt to parse date
        try:
            datetime.datetime.strptime(due_date, '%Y-%m-%d') #example date format
        except ValueError:
            messagebox.showerror("Error", "Incorrect date format, should be YYYY-MM-DD")
            return

        if task_to_edit:
            # Update existing task
            task_to_edit["description"] = description
            task_to_edit["category"] = category
            task_to_edit["priority"] = priority
            task_to_edit["due_date"] = due_date
            update_treeview() #refresh treeview
        else:
            # Add new task
            tasks.append({"description": description, "category": category, "priority": priority, "due_date": due_date})
            update_treeview() #refresh treeview

        window.destroy()

    tk.Button(window, text="Save", command=save_task).grid(row=4, column=0)
    tk.Button(window, text="Cancel", command=window.destroy).grid(row=4, column=1)

def exit_application():
    """Exits the application."""
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        main_window.destroy()

def update_treeview():
    """Updates the Treeview with the current tasks."""
    for item in tree.get_children():
        tree.delete(item)

    for task in tasks:
        tree.insert("", "end", values=(task["description"], task["category"], task["priority"], task["due_date"]))

def edit_selected_task():
    """Opens the Add/Edit window with the selected task's data."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a task to edit.")
        return

    item_values = tree.item(selected_item, "values")
    task_to_edit = {
        "description": item_values[0],
        "category": item_values[1],
        "priority": item_values[2],
        "due_date": item_values[3],
    }
    open_add_task_window(task_to_edit)

def delete_selected_task():
    """Deletes the selected task from the Treeview and the tasks list."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a task to delete.")
        return

    if messagebox.askokcancel("Confirm", "Are you sure you want to delete this task?"):
        item_values = tree.item(selected_item, "values")
        for task in tasks:
            if task["description"] == item_values[0] and task["category"] == item_values[1] and task["priority"] == item_values[2] and task["due_date"] == item_values[3]:
                tasks.remove(task)
                break
        tree.delete(selected_item)

# Main Window
main_window = tk.Tk()
main_window.title("Task Manager")

# Labels
tk.Label(main_window, text="Task Manager").pack(pady=10)

# Buttons
tk.Button(main_window, text="Add Task", command=open_add_task_window).pack(pady=5)
tk.Button(main_window, text="Edit Task", command=edit_selected_task).pack(pady=5)
tk.Button(main_window, text="Delete Task", command=delete_selected_task).pack(pady=5)
tk.Button(main_window, text="Filter").pack(pady=5)
tk.Button(main_window, text="Sort").pack(pady=5)
tk.Button(main_window, text="Exit", command=exit_application).pack(pady=5)

# Treeview
tree = ttk.Treeview(main_window, columns=("Description", "Category", "Priority", "Due Date"), show="headings")
tree.heading("Description", text="Description")
tree.heading("Category", text="Category")
tree.heading("Priority", text="Priority")
tree.heading("Due Date", text="Due Date")
tree.pack(pady=10)

# Image (Placeholder - add actual image later)
tk.Label(main_window, text="Image Placeholder").pack()

# Task data
tasks = []

main_window.mainloop()