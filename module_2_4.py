numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    count_delenii = 0
    if numbers[i] == 1:
        continue
    else:
        for k in range(len(numbers)):
            if numbers[k] > numbers[i]:
                break
            elif numbers[i] % numbers[k] == 0:
                count_delenii += 1
        if count_delenii > 2:
            not_primes.append(numbers[i])
        else:
            primes.append(numbers[i])
print('Обычные числа:', not_primes)
print('Простые числа:', primes)
