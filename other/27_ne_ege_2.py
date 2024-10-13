f = open("file")
n = int(f.readline())
a = [int(i) for i in f]

c = [0] * 60

for i in a:
    c[i % 60] += 1
r = sum([i * (i - 1) // 2 for i in c])
print(r)


# f = open("file")
# n = int(f.readline())
# a = [int(i) for i in f]

# k5 = n5 = 0

# for i in a:
#     if i % 5 == 0:
#         k5 += 1
# n5 = n - k5
# r = (
#     (k5 * (k5 - 1) * (k5 - 2) // 6)
#     + ((k5 * (k5 - 1) // 2) * n5)
#     + ((n5 * (n5 - 1) // 2) * k5)
# )
# print(r)  # Первый вариант (r=r1)
# r1 = (n * (n - 1) * (n - 2) // 6) - ((n5 * (n5 - 1) * (n5 - 2)) // 6)
# print(r1)  # Второй вариант (r=r1)


# f = open("file")
# n = int(f.readline())
# a = [int(i) for i in f]

# k2 = k3 = k6 = 0

# for i in a:
#     if i % 6 == 0:
#         k6 += 1
#     elif i % 2 == 0:
#         k2 += 1
#     elif i % 3 == 0:
#         k3 += 1
# n6 = n - k6
# r = k6 * n6 + k2 * k3 + k6 * (k6 - 1) // 2
# print(r)


# f = open("file")
# n = int(f.readline())
# a = [int(i) for i in f]

# c = [0]*10

# for i in a:
#     c[i%10]+=1
# print(c)
# r=c[1]*c[3]+c[7]*c[9]
# print(r)
