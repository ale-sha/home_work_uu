my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)
one = my_list.pop(0)
while one >= 0:
    if one == 0:
        one = my_list.pop(0)
        continue
    elif one > 0:
        print(one)
        one = my_list.pop(0)
    elif one < 0:
        break
