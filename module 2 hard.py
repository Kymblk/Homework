a = int(input('Введите число с камня: '))
str1 = ''
for i in range(1,a):
    for k in range(1 + i,a):
        res = i+k
        if a % res == 0:
            str1 += (str(i) + str(k))
print(f'Нужный пароль: {str1}')
