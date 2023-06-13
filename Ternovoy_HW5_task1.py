pib = input("Введіть свої Прізвище Ім'я По-батькові: ")
if pib.istitle() == True and pib.replace(' ', '').isalpha() == True:
    print('ПІБ складається з літер. Кожне слово починається з великої літери.')
elif pib.istitle() == True and pib.replace(' ', '').isalpha() == False:
    print('Кожне слово ПІБ починається з великої літери, але не всі слова складаються тільки з літер.')
elif pib.istitle() == False and pib.replace(' ', '').isalpha() == False:
    print('Не кожне слово ПІБ починається з великої літери, і не всі слова складаються тільки з літер.')
elif pib.istitle() == False and pib.replace(' ', '').isalpha() == True:
    print('Не кожне слово ПІБ починається з великої літери, але всі слова складаються тільки з літер.')