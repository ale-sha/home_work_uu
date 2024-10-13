import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides, filled=False):
        self.__sides = list(sides)
        self.__color = color
        self.filled = filled

        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        color = False
        if r >= 0 and g >= 0 and b >= 0:
            if r < 256 and g < 256 and b < 256:
                color = True
        if color:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *args):
        if self.sides_count != len(args):
            return False
        for side in args:
            if not isinstance(side, (int, float)) or side <= 0:
                return False
        return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = 0
        self.__sides = sides

    def get_radius(self):
        self.__radius = round(self.__len__() / (2 * math.pi), 2)
        return self.__radius

    def get_square(self):
        return round(math.pi * self.__radius ** 2, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)
        self.__sides = sides
        self.volume = 0

    def get_volume(self):
        self.volume = self.__sides[0] ** 3
        return self.volume


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print(cube1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


