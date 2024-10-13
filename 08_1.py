from itertools import *
alf = 'ДЕМОСТ'
c = permutations(alf, 6)
d=0
for i in c:
   s = ''.join(i)
   d+=1
   if d == 377:
      print(s)


# Все 5-буквенные слова, составленные из букв М,О,Р,Е записаны в алфавитном порядке. Вот начало списка:
# 1. ЕЕЕЕЕ
# 2. ЕЕЕЕМ
# 3. ЕЕЕЕО
# 4. ЕЕЕЕР
# 5. ЕЕЕМЕ
# .....
# Запишите слово, которое стоит под номером 433.

# from itertools import *
# alf = 'ЕМОР'
# c = product(alf, repeat=5)
# d=1
# for i in c:
#     s = ''.join(i)
#     #print(s)
#     if d == 433:
#        print(s)
#     d+=1