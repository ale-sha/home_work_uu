def apply_all_func(int_list, *functions):
    results = {}
    check = 0
    for i in int_list:
        if isinstance(i, (int, float)):
            check += 1
    if check == len(int_list):
        for func in functions:
            results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6.0, 20, '15', 9], max, min))
print(apply_all_func([6, 20, 15.9, 9], len, sum, sorted))
