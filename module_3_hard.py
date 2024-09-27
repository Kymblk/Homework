def count_elements(data):
    t_sum = 0
    stack = data.copy()  # Используем стек для хранения элементов для обработки

    while stack:
        current = stack.pop()  # Извлекаем текущий элемент

        if isinstance(current, (int, float)):
            t_sum += current
        elif isinstance(current, str):
            t_sum += len(current)
        elif isinstance(current, dict):
            for key, value in current.items():
                if isinstance(key, str):
                    t_sum += len(key)
                stack.append(value)  # Добавляем значение для дальнейшей обработки
        elif isinstance(current, (list, tuple, set)):
            stack.extend(current)  # Добавляем все элементы для дальнейшей обработки
    return t_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(count_elements(data_structure))