def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Поиск минимального элемента
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Обмен минимального элемента с текущим
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Вывод текущего состояния массива
        print(arr)

# Исходный массив
arr = [-4, -2, 2, 3, 6, 8]

# Вызов сортировки
selection_sort(arr)