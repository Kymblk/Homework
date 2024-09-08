immutable_var = (1, 2, 3, True, 'qwerty', [4, 5, 6])
print(immutable_var)
try:
    immutable_var[2] = 'new'    
except TypeError:
    print(immutable_var)  # при выводе на экран видим, что кортеж не изменился
# Использовал try - except чтобы код не остановился при ошибке. При попытке изменить элемент кортежа
# Вылезет ошибка TypeError т.к кортеж является неизменяемым контейнером для хранения данных в отличии от списков

mutable_list = ['a', 2, True]
mutable_list[0] = 'bc'
mutable_list[1] = 17
print(mutable_list)