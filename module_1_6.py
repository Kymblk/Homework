my_dict = {
    'Vasya': 1975,
    'Egor': 1999,
    'Masha': 2002
}
print(f'Dict: {my_dict}')
print('Existing value: ', my_dict.get('Vasya'))  # значение по существующему ключу
print('Not existing value: ', my_dict.get('Grigoriy'))  # значение по отсутствующему ключу

my_dict['Ruslam'] = 2003  # добавление новой пары
my_dict['Artem'] = 2001  # добавление новой пары

print('Deleted value: ', my_dict.pop('Egor'))  # удаление пары в словаре по ключу
print(f'Modified dict: {my_dict}')

my_set = {1, 2, 2, True, 'abc', 'abc'}
print(f'Set: {my_set}')

my_set.update([777, 666])
my_set.pop()
print(f'Modified set: {my_set}')