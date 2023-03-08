# word = "Python"
# word = "maks"
# vowels = set("aeiouy")
# word_set = set(word.lower())

# print('Гласных {}, согласных {}'.format(len(word_set.intersection(vowels)),
#                                         len(word_set.difference(vowels))))


quest = int(input('Сколько будет строк? '))
gls = 0
sgl = 0
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
while quest > count:
    poem = input()
    for i in poem:
        if i.isalpha():
            if i in vse_gls:
                gls += 1
            else:
                sgl += 1
    count += 1

print('Кол-во гласных:', gls)
print('Кол-во согласных:', sgl)

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
# rus = "йцукенгшщзхъфывапролджэячсмитьбюё"

# while True:
#     word = input('\nenter word: ')
#     if word == 'exit' or word == 'выход':
#         break
#     for i in word:
#         if i in eng:
#             print(rus[eng.index(i)], end='')


# print(rus.index('н'))
# print(eng[rus.index('й')])
