# циклы
# [start:stop:step]
# print(word[::3])
# print(word[4:7:1])
# i - item, iterable

# for i in range(1, 11):
#     print(i)

eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
rus = "йцукенгшщзхъфывапролджэячсмитьбюё"

while True:
    word = input('\nenter word: ')
    if word == 'exit' or word == 'выход':
        break
    for i in word:
        if i in eng:
            print(rus[eng.index(i)], end='')


print(rus.index('н'))
print(eng[rus.index('й')])


# eybdthcbntn
# ещьщккщц


# while True:
#     cash = int(input('enter sum: '))
#     years = int(input('enter years: '))
#     percents = float(input('enter %'))
#
#     for year in range(1, years+1):
#         casha = cash * percents
#         cash += casha
#         print(f'year: {year} ==> {cash}')


# print(cash * percents)


# symbols = "!@#$%^&*()_+"
# print('q' in 'python')
# objects = '2q#w?3п1в(а;п7'

# for object in objects:
#     if object.isnumeric():
#         print(object, 'number')
#     elif object.isalpha():
#         print(object, 'alphabet')
#     elif object in symbols:
#         print(object, 'symbol')
#     else:
#         print('unknown object!')


# word = 'programming'
#
# for letter in word:
#     if letter == 'm':
#         continue
#     print(letter, end='')


# attempts = 5
#
# while attempts > 0:
#     temperature = input(f'enter degree: осталось {attempts} попыток')
#     if temperature == 'exit':
#         print('goodbay!')
#         break
#     temperature = int(temperature)
#
#     if temperature >= -40 and temperature <= 10:
#         print('холодно')
#     elif temperature >= 11 and temperature <= 20:
#         print('прохладно')
#     elif temperature >= 21 and temperature <= 27:
#         print('тепло')
#     elif temperature >= 28 and temperature <= 52:
#         print('жарко')
#     else:
#         print('Че за погода, ваа!')
#     attempts -= 1


# rounds = 10
#
# while rounds > 0:
#     print(f'круг, {rounds}')
#     if rounds == 6:
#         break
#     rounds -= 1

# c = 0
#
# while c < 100:
#     c += 1
#     if c % 2 == 0:
#         continue
#     print('hello', c)
