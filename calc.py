import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, pady=5)
        button_frame = tk.Frame(root)
        button_frame.pack()
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(button_frame, text=text, font=("Arial", 14), width=5, height=2,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)
        clear_btn = tk.Button(root, text="C", font=("Arial", 14), width=25, height=2, command=self.clear)
        clear_btn.pack(pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += char
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
