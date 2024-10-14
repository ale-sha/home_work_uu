def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding="utf-8")
    count_line = 0
    new = []
    for line in strings:
        count_line += 1
        cursor = file.tell()
        my_tuple = (count_line, cursor)
        file.write(line + '\n')
        my_dict = (my_tuple, line)
        new.append(my_dict)
    file.close()
    diction = dict(new)
    return diction


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
