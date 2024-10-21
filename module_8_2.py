def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            if isinstance(number, (int, float)):
                result += number
            else:
                incorrect_data += 1
    except TypeError:
        incorrect_data = len(numbers)
        print(f'В numbers записан некорректный тип данных')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_num, incorrect_data = personal_sum(numbers)
        valid_num = len(numbers) - incorrect_data
        if valid_num == 0:
            return 0
        return sum_num / valid_num
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
