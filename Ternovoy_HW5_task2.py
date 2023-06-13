list_of_num = [int(i) for i in input("Введіть не менше п'яти чисел через пробіл: ").split()]
if len(list_of_num) >= 5:
    summa = list_of_num[1] + list_of_num[-2] + sum(list_of_num) / len(list_of_num)
    print(f'Cума другого, передостаннього, а також середнього арифметичного значення даної послідовності - {summa}')
else:
    print("Введено менше п'яти чисел!")