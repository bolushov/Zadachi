from tkinter import *

# Функция для обработки нажатия кнопок
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Ошибка")

# Создание окна
root = Tk()
root.title("Калькулятор")
root.configure(bg='lightblue')

# Создание поля ввода
entry = Entry(root, width=20, borderwidth=5, font=('Arial', 16), bg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Создание кнопок
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
           command=lambda btn=button: button_click(btn) if btn != '=' else calculate(),
           bg='lightgray', fg='black').grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

Button(root, text='C', padx=20, pady=20, command=clear, font=('Arial', 14), bg='red', fg='white').grid(row=5, column=0, columnspan=4)

root.mainloop()