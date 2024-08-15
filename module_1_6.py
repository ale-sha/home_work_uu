my_dict = {'dog' : 4, 'snake' : 0, 'spider' : 8}
print(my_dict)
print(my_dict['dog'])
print(my_dict.get('human'))
my_dict.update({'bird' : 2,
                'beetlе' : 6})
print(my_dict)
no_legs = my_dict.pop('snake')
print(no_legs)
print(my_dict)

my_set = {1, 11, False, 'sun', 1, False, 5.9}
print(my_set)
my_set.update({5, 'moon'})
my_set.discard(1)
print(my_set)

