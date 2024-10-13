from itertools import permutations

count = set()

for x in permutations('01234567'):
    s = ''.join(x)
    # проверка, что число не начинается с 0 и при этом две чётных или нечётных цифры не стоят рядом
    if s[0] != '0' and all(int(s[i]) % 2 != int(s[i+1]) % 2 for i in range(len(s)-1)):
        count.add(s)
print(len(count))