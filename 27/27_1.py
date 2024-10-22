f = open("file")
n = int(f.readline())
a = [int(i) for i in f]

m = [0] * 60
ms = 0
for i in range(n - 1):
    if a[i] > m[a[i] % 60]:
        m[a[i] % 60] = a[i]
    t = (60 - (a[i + 1] % 60)) % 60
    if m[t] + a[i + 1] > ms and (m[t] > 0):
        ms = m[t] + a[i + 1]
print(ms)


# f = open("file")
# n = int(f.readline())
# a = [int(i) for i in f]

# m1 = m2 = m3 = m6 = maxp = 0

# for i in range(n - 1):
#     m1 = max(m1, a[i])
#     if a[i] % 2 == 0:
#         m2 = max(a[i], m2)
#     if a[i] % 3 == 0:
#         m3 = max(a[i], m3)
#     if a[i] % 6 == 0:
#         m6 = max(a[i], m6)
#     if (m1 * a[i + 1]) % 6 == 0:
#         maxp = max((m1 * a[i + 1]), maxp)
#     if (m2 * a[i + 1]) % 6 == 0:
#         maxp = max((m2 * a[i + 1]), maxp)
#     if (m3 * a[i + 1]) % 6 == 0:
#         maxp = max((m3 * a[i + 1]), maxp)
#     if (m6 * a[i + 1]) % 6 == 0:
#         maxp = max((m6 * a[i + 1]), maxp)
# print(maxp)


# f = open("file")
# n = int(f.readline())
# a = [int(i) for i in f]

# mc = mn = maxs = 0

# for i in range(n - 1):
#     if (a[i] > mc) and (a[i] % 2 == 0):
#         mc = a[i]
#     if (a[i] > mn) and (a[i] % 2 != 0):
#         mn = a[i]
#     if (mc + a[i + 1] > maxs) and ((mc + a[i + 1]) % 2 == 0):
#         maxs = mc + a[i + 1]
#     if (mn + a[i + 1] > maxs) and ((mn + a[i + 1]) % 2 == 0):
#         maxs = mn + a[i + 1]
# print(maxs)
