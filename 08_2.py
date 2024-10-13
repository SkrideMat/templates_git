from itertools import *
alf = 'КОСУФ'
c = product(alf, repeat=5)
d=0
for i in c:
    s = ''.join(i)
    d+=1
    if s.count('У')==2 and not 'Ф' in s:
        print(d)      

# Артём составляет 5-буквенные слова из букв О, П, Е, Р, А. Каждая буква может встречаться ровно один раз. При этом в слове не могут стоять рядом две согласные буквы, а буква П не может стоять на первом или последнем месте. Словом считается любая допустимая последовательность букв, не обязательно осмысленная. Сколько слов может составить Артём?
# from itertools import *
# alf = 'ОПЕРА'
# c = permutations(alf, 5)
# d=set()
# for i in c:
#     s = ''.join(i)
#     if s[0]!='П' and s[-1]!='П' and not 'ПР' in s and not 'РП' in s:
#         d.add(s)
# print(len(d))


# Пашка составляет 5-буквенные слова из букв П, А, Р, Е, К. Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов может составить Пашка?
# from itertools import permutations

# count = set()

# gl = ’АЕ’

# for x in permutations(’ПАРЕК’):
#     s = ’’.join(x)
#     # проверка, что в слове нет подряд идуших гласных или согласных букв
#     if all((s[i] in gl) != (s[i+1] in gl) for i in range(len(s)-1)):
#         count.add(s)
# print(len(count))             