f = open("file")
n = int(f.readline())
a = [int(i) for i in f]

mc = mn = maxs = 0

for i in range(n - 1):
    if (a[i] > mc) and (a[i] % 2 == 0):
        mc = a[i]
    if (a[i] > mn) and (a[i] % 2 != 0):
        mn = a[i]
    if (mc + a[i + 1] > maxs) and ((mc + a[i + 1]) % 2 == 0):
        maxs = mc + a[i + 1]
    if (mn + a[i + 1] > maxs) and ((mn + a[i + 1]) % 2 == 0):
        maxs = mn + a[i + 1]
print(maxs)
