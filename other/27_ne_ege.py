f = open("file")
n = int(f.readline())
a = [int(i) for i in f]
k7m = k7 = 0
m = [0] * 7
for i in a:
    if i % 7 == 0:
        if i > k7m:
            k7 = k7m
            k7m = i
        elif i > k7:
            k7 = i
    if i > m[i % 7]:
        m[i % 7] = i
print(m)
for i in range(1, 4):
    s = m[i] + m[7 - i]
    print(s)
