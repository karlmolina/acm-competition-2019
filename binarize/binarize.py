file = open('binarize.in')

num = int(file.readline())

out = open('binarize.out', 'w')

for i in range(num):
    value = int(file.readline())
    string = f"Input value: {value}"
    out.write(f"Input value: {value}\n")
    n = 1
    while n < value:
        n *= 2
    out.write(str(n) + '\n')
    out.write('\n')

