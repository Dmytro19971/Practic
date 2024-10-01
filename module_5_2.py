class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title

hightower = House('ЖК Grey', 12)
warehouse = House('Склад', 4)

print(hightower)
print(warehouse)

print(len(hightower))
print(len(warehouse))