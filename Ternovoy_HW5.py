# Task 1

pib = input("Введіть свої Прізвище Ім'я По-батькові: ")
if pib.istitle() == True and pib.replace(' ', '').isalpha() == True:
    print('ПІБ складається з літер. Кожне слово починається з великої літери.')
elif pib.istitle() == True and pib.replace(' ', '').isalpha() == False:
    print('Кожне слово ПІБ починається з великої літери, але не всі слова складаються тільки з літер.')
elif pib.istitle() == False and pib.replace(' ', '').isalpha() == False:
    print('Не кожне слово ПІБ починається з великої літери, і не всі слова складаються тільки з літер.')
elif pib.istitle() == False and pib.replace(' ', '').isalpha() == True:
    print('Не кожне слово ПІБ починається з великої літери, але всі слова складаються тільки з літер.')


# Task 2

list_of_num = [int(i) for i in input("Введіть не менше п'яти чисел через пробіл: ").split()]
if len(list_of_num) >= 5:
    summa = list_of_num[1] + list_of_num[-2] + sum(list_of_num) / len(list_of_num)
    print(f'Cума другого, передостаннього, а також середнього арифметичного значення даної послідовності - {summa}')
else:
    print("Введено менше п'яти чисел!")


# Task 3

red = int(input('Введіть червону складову кольору RGB (від 0 до 255 включно): '))
green = int(input('Введіть зелену складову кольору RGB (від 0 до 255 включно): '))
blue = int(input('Введіть синю складову кольору RGB (від 0 до 255 включно): '))
tuple_rgb = (red, green, blue)
print(f'RGB колір - {tuple_rgb}')


# Task 4

from collections import namedtuple, deque

Marks = namedtuple('Marks', ['Algebra', 'Geometry', 'History', 'Informatics', 'Geography'])
marks = deque([
    Marks(9, 10, 9, 11, 11),
    Marks(6, 7, 7, 6, 12),
    Marks(10, 10, 11, 10, 11),
    Marks(5, 6, 5, 5, 4)
])
for mark in marks:
    print(mark)


# Task 5

list_of_num = [int(i) for i in input('Введіть будь-яку кількість чисел через пробіл: ').split()]
tuple_of_num = tuple(list_of_num)
sort_tuple_of_num = tuple(sorted(tuple_of_num))
print(f'Відсортований кортеж з уведених чисел - {sort_tuple_of_num}')


# Task 6

priklad_vidguku = '''Закритий комплекс зі своїм пляжем. Дуже красива територія - зелена та доглянута.
                     В номерах число, комфортно. Меню різноманітне та вишукане. Обслуговування на
                     найвищому рівні. Є спортзал, басейн, солярій, сауна.'''
znuzhka = 0
if 'меню' in priklad_vidguku:
    znuzhka += 5
if 'спортзал' in priklad_vidguku:
    znuzhka += 5
if 'обслуговування' in priklad_vidguku:
    znuzhka += 5
if len(priklad_vidguku) > 60:
    znuzhka += 15
print(f'Ваша знижка на натупний заїзд сягає {znuzhka}%')