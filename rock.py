import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if choice == computer_choice:
        result = "It's a Draw!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x400")
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=20)
tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=10)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=10)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=30)

root.mainloop()
