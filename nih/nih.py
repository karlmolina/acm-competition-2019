file = open('nih.in')

num = int(file.readline())

out = open('nih.out', 'w')


class Disease:
    def __init__(self, l):
        self.data = []
        # self.data = [[l[0], l[2], l[4], l[6]], [l[1], l[3], l[5], l[7]]]
        # self.data = [[l[0], l[1]], [l[2], l[3]], [l[4], l[5]], [l[6], l[7]]]

        for i in range(0, 8, 2):
            self.data.append(BreakPoint(l[i], l[i + 1]))

    def __repr__(self):
        return ', '.join([str(i) for i in self.data])


class BreakPoint:
    def __init__(self, funding, lives):
        self.funding = int(funding)
        self.lives = int(lives)

    def __repr__(self):
        return f'{self.funding} : {self.lives}'


def max(a, cost):
    disease = a[0]
    if len(a) == 1:
        temp = 3
        while temp > 0 and cost < disease.data[temp].funding:
            temp -= 1

        if disease.data[temp].funding <= cost:
            return disease.data[temp].lives
        return 0

    result = max(a[1:], cost)
    rc=result
    if rc == 0:
        return max([a[0]], cost)
    print(rc)
    for i in range(4):
        if cost >= disease.data[i].funding:
            if disease.data[i].funding + rc <= cost:
                if result < disease.data[i].lives + rc:
                    result = disease.data[i].lives + rc
                    print(' ',disease.data[i].lives,result)
            else:
                temp = max(a[1:], cost - disease.data[i].funding)
                if result < disease.data[i].lives + temp:
                    result = disease.data[i].lives + temp
        else:
            break
        i+=1

    return result


for budget in range(num):
    line = file.readline().split(' ')
    num_disease = int(line[0])
    money = int(line[1])
    diseases = []

    for i in range(num_disease):
        l = file.readline().split(' ')
        disease = Disease(l)
        diseases.append(disease)

    print(diseases)

    lives = max(diseases, money)

    out.write(f"Budget #{budget+1}: Maximum of {lives} lives saved.\n\n")
