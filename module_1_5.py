immutable_var = (23, "cat", True, 5.5)
print(immutable_var)
#immutable_var[2] = False
#print(immutable_var)  мы не можем изменять данные в кортеже, потому что он имеет неизменяемый тип данных
mutable_list = [23, "cat", True, 5.5]
mutable_list.append(4)
mutable_list[1] = 'dog'
print(mutable_list)

