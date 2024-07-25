# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
      print(a, b, c)
print_params()

# 2.Распаковка параметров:
values_list = [1, 'строка', True]
print_params(*values_list)

values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
values_dict_2 = {'c': 42}
print_params(*values_list_2,**values_dict_2)

