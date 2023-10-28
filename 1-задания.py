# Шаг 1
my_string = "Илим выбрал"

# Шаг 2
NUM = 2

# Шаг 3
word = "ты молодец"

# Шаг 4
result = str(NUM) + " " + word

# Шаг 5
print( my_string, result)

# Шаг 6
if NUM < 0:
    print("Вы сохранили отрицательное число")
elif NUM > 0:
    print("Вы сохранили положительное число")
else:
    print("Вы сохранили ноль")

# Дополнительное задание (СРС)
print("Введите ваше имя:")
user_name = input()
print("Привет, " + user_name + "!")