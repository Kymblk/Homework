def get_multiplied_digits(number):
    if number == 0:
        return 0
    str_number = str(int(number)).replace('0','')
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))
print(get_multiplied_digits('00203'))
print(get_multiplied_digits('20300'))
print(get_multiplied_digits(400))
print(get_multiplied_digits(0))

