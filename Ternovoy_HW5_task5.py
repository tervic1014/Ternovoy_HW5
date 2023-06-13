list_of_num = [int(i) for i in input('Введіть будь-яку кількість чисел через пробіл: ').split()]
tuple_of_num = tuple(list_of_num)
sort_tuple_of_num = tuple(sorted(tuple_of_num))
print(f'Відсортований кортеж з уведених чисел - {sort_tuple_of_num}')