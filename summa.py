from tkinter import *

root = Tk()
root.title('Сумма чисел между')
root.geometry("500x250")  # Увеличил высоту окна для лучшего отображения

# Функция для вычисления суммы чисел между a и b
def summa():
    try:
        a = int(EntryA.get())
        b = int(EntryB.get())
        if a > b:
            a, b = b, a  # Обмен a и b, если a > b
        sum_numbers = sum(range(a, b + 1))
        result_label['text'] = f'Сумма чисел от {a} до {b} равна {sum_numbers}'
    except ValueError:
        result_label['text'] = 'Ошибка ввода'

Label(root, text='Первое число').grid(row=0, sticky=W)
Label(root, text='Второе число').grid(row=1, sticky=W)

EntryA = Entry(root, width=10, font=('Arial', 16))
EntryA.grid(row=0, column=1, sticky=E)

EntryB = Entry(root, width=10, font=('Arial', 16))
EntryB.grid(row=1, column=1, sticky=E)

result_label = Label(root, width=30, font=('Arial', 16), fg='blue')  # Изменил цвет текста
result_label.grid(row=2, columnspan=2, pady=10)  # Добавил отступ вниз

calculate_button = Button(root, text='Вычислить сумму', command=summa, font=('Arial', 16), bg='green', fg='white')  # Изменил цвет кнопки
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)  # Добавил отступ вниз

root.mainloop()
