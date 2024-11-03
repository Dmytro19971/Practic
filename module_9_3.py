first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
#print(first)
#print(second)


first_result = [(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y)]
print(first_result)

second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
print(second_result)