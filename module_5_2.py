class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                return
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


my_home_1 = House("жк Ромашка", 15)
my_home_2 = House('жк Развалюшка', 3)

print(my_home_1)
print(len(my_home_1))
print(my_home_2)
print(len(my_home_2))
