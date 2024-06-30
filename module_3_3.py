# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # при вызове без аргументов выводятся параметры по умолчанию
print_params(2, 'City', False)  # вызов большего числа параметров, чем задано в функции, приводит к ошибке
print_params(2)  # если задается при вызове функции один или два параметра, то остальные выводятся по умолчанию
print_params(5, 'City')
print_params(b=25)  # новые параметры выводятся на заданных местах, но PC "ругается": ждал сроку, получил число и т.д.
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = ['hello', 8, True]
values_dict = {'a': 5, 'b': 'Город', 'c': 30}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
