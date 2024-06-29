import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO-LIST")
        self.tasks = []
        #Create the main frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        #Create the listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, height=15, width=50, bd=0,selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        #add a scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        #Create an entry widget to add new tasks
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        #Add buttons to add and delete tasks
        self.add_task_button = tk.Button(root, text="Add Task", width=48, command=self.add_task)
        self.add_task_button.pack(pady=5)
        self.delete_task_button = tk.Button(root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_task_button.pack(pady=5)
    def add_task(self):
       task = self.task_entry.get()
       print(f"Task entered:{task}")
       if task != "":

           self.tasks.append(task)
           print(f"Task lists:{self.tasks}")
           self.update_task_list()
           self.task_entry.delete(0, tk.END)
       else:
           messagebox.showwarning("Warning!You must enter a task.")
    def delete_task(self):
       try:
           selected_task_index = self.task_listbox.curselection()[0]
           self.tasks.pop(selected_task_index)
           self.update_task_list()
       except IndexError:
           messagebox.showwarning("Warning!You must select a task.")
    def update_task_list(self):
       self.task_listbox.delete(0, tk.END)
       for task in self.tasks:
           self.task_listbox.insert(tk.END, task)
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
    
       

