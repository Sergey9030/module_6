class Animal:     # животные

    def __init__(self, name):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name  # индивидуальное название каждого животного


class Plant:        # растения

    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):  # млекопитающие

    def eat(self, food):  # food is Plant (растение):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Predator(Animal):  # хищники

    def eat(self, food):  # food is Plant (растение):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True



class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
