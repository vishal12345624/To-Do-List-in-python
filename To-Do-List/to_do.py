from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Main window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="lightblue")

# Heading
Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="lightblue").pack(pady=10)

# Entry field to add new tasks
task_entry = Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=10, padx=20, fill=X)

# Listbox to show tasks
task_listbox = Listbox(root, font=("Helvetica", 14), selectbackground="gray", selectforeground="white")
task_listbox.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Scrollbar for the listbox
scrollbar = Scrollbar(task_listbox)
scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Function to add task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        showwarning("Input Error", "Task cannot be empty.")

# Function to delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        showwarning("Selection Error", "Please select a task to delete.")

# Function to save tasks to file
def save_tasks():
    tasks = task_listbox.get(0, END)
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    showinfo("Saved", "Tasks saved successfully!")

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for task in f.readlines():
                task_listbox.insert(END, task.strip())

# Function to edit selected task
def edit_task():
    try:
        selected_index = task_listbox.curselection()[0] 
        old_task = task_listbox.get(selected_index)      

        task_entry.delete(0, END)
        task_entry.insert(0, old_task)

        task_listbox.delete(selected_index)

    except IndexError:
        showwarning("Selection Error", "Please select a task to edit.")


# Buttons
button_frame = Frame(root, bg="lightblue")
button_frame.pack(pady=10)

add_btn = Button(button_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

save_btn = Button(button_frame, text="Save Tasks", width=12, command=save_tasks)
save_btn.grid(row=1, column=0, padx=5, pady=5)

edit_btn = Button(button_frame, text="Edit Task", width=12, command=edit_task)
edit_btn.grid(row=1, column=1,  padx=5, pady=5)

exit_btn = Button(button_frame, text="Exit", width=12, command=root.destroy)
exit_btn.grid(row=2, column=0, columnspan=2, pady=5)

# Load tasks on startup
load_tasks()

# Run the app
root.mainloop()
