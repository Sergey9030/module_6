import math

def is_side(v):  # Проверяет, что v целое и положительное ()
    if isinstance(v, int) and v >= 0:
        return True
    else:
        return False


def is_color(v):  # Проверяет, что v целое и находится в диапазоне 0-255
    if isinstance(v, int) and (0 <= v <= 255):
        return True
    else:
        return False


class Figure:
    sides_count = 0

    def __init__(self, c, *args):
        self.__sides = []
        if self.__is_valid_sides(*args):
            self.set_sides(*args)
        elif len(args) == 1:
            v = []
            for i in range(self.sides_count):
                v.append(args[0])
            self.set_sides(*v)
        else:
            v = []
            for i in range(self.sides_count):
                v.append(1)
            self.set_sides(*v)

        if self.__is_valid_color(*c):
            self.set_color(*c)
        else:
            self.set_color = [255, 255, 255]

        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if is_color(r) and is_color(g) and is_color(b):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if self.sides_count == len(args):
            for i in args:
                if not is_side(i):
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        v = 0
        for i in self.__sides:
            v += i
        return v

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, c, *args):
        super().__init__(c, *args)
        self.__radius = len(self.get_sides())/2/math.pi

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self, c, *args):
        super().__init__(c, *args)
        s = self.get_sides()
        # Вычисляем высоту по первой стороне.
        # Если теугольник не равносторонний для остальных сторон результат буден другой.
        self.__height = self.get_square()*2/s[0]

    def get_height(self):
        return self.__height
    def get_square(self):
        p = len(self)/2
        s = self.get_sides()
        return math.sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2]))  # Формула Герона


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

