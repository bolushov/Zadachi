import tkinter as tk
import random

def increase_counter():
    current_value = int(counter_label['text'])
    new_value = current_value + 1
    update_counter(new_value)

def decrease_counter():
    current_value = int(counter_label['text'])
    new_value = current_value - 1
    update_counter(new_value)

def update_counter(new_value):
    counter_label['text'] = str(new_value)
    counter_label['fg'] = random.choice(["red", "green", "blue", "orange", "purple"])

root = tk.Tk()
root.title("Простой счетчик")
root.geometry("200x100")

counter_label = tk.Label(root, text="0", font=("Arial", 24), fg="black")
counter_label.pack(pady=20)

increment_button = tk.Button(root, text="Увеличить", command=increase_counter)
increment_button.pack(side="left")

decrement_button = tk.Button(root, text="Уменьшить", command=decrease_counter)
decrement_button.pack(side="right")

root.mainloop()
