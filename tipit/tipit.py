file = open('tipit.in')

num = int(file.readline())

out = open('tipit.out', 'w')

import math

def isPali(n):
    ncopy = n
    out = 0
    while n > 0:
        out *= 10
        out += n % 10
        n = int(n / 10)
        # print(n)
    return ncopy == out


for i in range(num):
    value = int(file.readline())
    out.write(f"Input cost: {value}\n")

    k = math.ceil(value / 5)
    while not isPali(value + k):
        k += 1

    out.write(f"{k} {value+k}\n\n")

out.close()