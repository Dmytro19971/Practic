def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5)
print_params(10, 'hello')
print_params(20, 'world', False)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [10, 'string2', False]
values_dict = {'a': 5, 'b': 'dict_v', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'string']
print_params(*values_list_2, 42)


