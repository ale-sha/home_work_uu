def summinstor(*args):
    sum = 0
    for arg in args:
        if isinstance(arg, dict):
            sum += summinstor(tuple(arg.items()))
        elif isinstance(arg, (list, set, tuple)):
            for i in arg:
                sum += summinstor(i)
        elif isinstance(arg, str):
            sum += len(arg)
        else:
            sum += arg
    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
  ]

print(summinstor(data_structure))
