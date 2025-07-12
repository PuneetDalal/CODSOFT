import tkinter

class Todolist:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.entry = tkinter.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill="x")
        add_button = tkinter.Button(root, text="Add Task", font=("Arial", 12), command=self.add_task)
        add_button.pack(pady=5)

        self.tasks_frame = tkinter.Frame(root)
        self.tasks_frame.pack(fill="both", expand=True, pady=10)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text == "":
            return
        task_frame = tkinter.Frame(self.tasks_frame)
        task_frame.pack(fill="x", pady=2, padx=5)
        var = tkinter.IntVar()
        checkbox = tkinter.Checkbutton(task_frame, text=task_text, variable=var, font=("Arial", 12), anchor="w")
        checkbox.pack(side="left", fill="x", expand=True)
        del_button = tkinter.Button(task_frame, text="Delete", font=("Arial", 10), command=lambda: self.delete_task(task_frame))
        del_button.pack(side="right")

        self.entry.delete(0, tkinter.END)

    def delete_task(self, task_frame):
        task_frame.destroy()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = Todolist(root)
    root.mainloop()
