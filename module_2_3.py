my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
indx = 0

while indx < len(my_list):
    if my_list[indx] == 0:
        indx += 1
        continue
    elif my_list[indx] > 0:
        print(my_list[indx])
        indx += 1
    else:
        break
        