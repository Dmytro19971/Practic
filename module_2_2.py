first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and first == third and second == third:
    print(3)
elif first != second and first == third or second == third or first == second:
    print(2)
else:
    print(0)
