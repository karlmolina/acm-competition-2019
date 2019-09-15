file = open('texting.in')

out = open('texting.out', 'w')

abb = int(file.readline())

dict = {}

for i in range(abb):
    line = file.readline().split(' ')
    dict[line[0]] = ' '.join(line[1:]).strip()

# print(dict)

p = int(file.readline())
for i in range(p):
    line = file.readline().split(' ')
    for word in line:
        word = word.strip()
        if word in dict.keys():
            out.write(dict[word] + ' ')

        else:
            out.write(word + ' ')
    out.write('\n')
