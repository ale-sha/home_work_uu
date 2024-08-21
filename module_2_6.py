import random

stone_one = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random_value = random.choice(stone_one)
print(f'На поле выпало: {random_value}')


def consist_value(n):
    examples_str = ''
    list_num = []
    for i in range(n - 1):
        list_num.append(i + 1)
    examples = []
    for i in range(len(list_num)):
        list_1 = []
        examples.append(list_1)
        for j in range(len(list_num)):
            if i > len(list_num) / 2 - 1:
                break
            elif list_num[i] == list_num[j] == n / 2 or list_num[i] == list_num[j]:
                continue
            elif i > j:
                continue
            elif n % (list_num[i] + list_num[j]) == 0:
                list_1.append(list_num[i])
                list_1.append(list_num[j])
                continue
            else:
                continue
        examples_str = ''.join([str(elem) for elem in sum(examples, [])])
    return examples_str


print(f'Подходящий пароль: {consist_value(random_value)}')
