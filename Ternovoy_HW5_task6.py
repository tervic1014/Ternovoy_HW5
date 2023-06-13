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