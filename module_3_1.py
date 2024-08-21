calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    length = len(string)
    lower_case = []
    upper_case = []
    count_calls()
    for i in range(len(string)):
        if string[i].isupper():
            lower_case.append(string[i])
        else:
            upper_case.append(string[i])
    return print((length, lower_case, upper_case))


def is_contains(string, list_to_search):
    count_calls()
    one = string.lower()
    two = [x.lower() for x in list_to_search]
    if two.__contains__(one):
        print(True)
    else:
        print(False)
    return print()


a = 'Жили у Бабуси'
b = ['Жили у бабуси', 'два веселых гуся']
c = 'Одинокие дома'
d = ['Зима, холода', "одинокие дома"]
is_contains(c, d)
is_contains(a, b)
string_info(a)
string_info(c)

print(calls)