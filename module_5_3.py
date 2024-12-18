class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        return NotImplemented

    def __len__(self):
        return self.number_of_floors

    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # eq

h1 = h1 + 10 # add
print(h1)
print(h1 == h2)

h1 += 10 # iadd
print(h1)

h2 = 10 + h2 # radd
print(h2)

print(h1 > h2) # gt
print(h1 >= h2) # ge
print(h1 < h2) # lt
print(h1 <= h2) # le
print(h1 != h2) # ne