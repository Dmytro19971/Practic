class Vehicle:
    __color_variants = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Pink']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        new_color = input('Новый цвет: ')
        reg_colours = [color.lower() for color in self.__color_variants]
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

class Sedan(Vehicle):
    __passengers_limit = 4

avto1 = Sedan('Dima', 'BMW 320', 224, 'Blue')

avto1.print_info()

avto1.set_color('Gray')
avto1.set_color('Black')
avto1.owner = 'Valentina'

avto1.print_info()