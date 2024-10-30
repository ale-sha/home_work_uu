def is_prime(func):
    def compound_num(*args):
        number = func(*args)
        if number < 2:
            print("Составное")
        count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
        if count == 2:
            print("Простое")
        else:
            print("Составное")
    return compound_num


@is_prime
def sum_three(a, b, c):
    summ = a + b + c
    return summ


result = sum_three(2, 3, 6)
# print(result)
