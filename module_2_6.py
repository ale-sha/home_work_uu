import random

stone_one = list(range(3, 21))
print(stone_one)
random_value = random.choice(stone_one)
print(f'На поле выпало: {random_value}')


def consist_value(n):
    list_num = list(range(1, n))
    examples = []
    for i in range(len(list_num)//2):
        for j in range(i + 1, len(list_num)):
            if n % (list_num[i] + list_num[j]) == 0:
                examples += [list_num[i], list_num[j]]
    return ''.join(map(str, examples))


print(f'Подходящий пароль: {consist_value(6)}')
