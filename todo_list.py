import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        self.tasks = self.load_tasks()

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.load_tasks_to_listbox()

    def load_tasks(self):
        try:
            with open('todo_list.json', 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open('todo_list.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.load_tasks_to_listbox()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Update the task:", initialvalue=self.tasks[selected_index])
            if new_task:
                self.tasks[selected_index] = new_task
                self.save_tasks()
                self.load_tasks_to_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.save_tasks()
            self.load_tasks_to_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
    