
name = input('What is your name? ')
age_c = input('How old are you? ')
age_i = int(age_c)

year = 2021 - int(age_i)

print('Hello ' + name + '. You where born at ' + str(year))


if age_i > 10:
    print('Menor de 10')
else:
    print('Mayor de 10')

print('Fin')