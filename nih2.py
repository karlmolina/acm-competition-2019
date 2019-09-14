class Disease:
    def __init__(self):
        self.investment = None

class Investment:
    def __init__(self, cost, lives, disease):
        self.disease = int(disease)
        self.lives = int(lives)
        self.cost = int(cost)



file = open('nih.in')
num = int(file.readline())
out = open('nih.out', 'w')

for budget in range(num):
    line = file.readline().split(' ')
    num_disease = int(line[0])
    money = int(line[1])
    diseases = []
    investments = []

    for i in range(num_disease):
        l = file.readline().split(' ')
        diseases.append(Disease())
        for j in range(4):
            investments.append(Investment(l[2 * j], l[2 * j + 1], i))

    print(investments)
    investments=sorted(investments, key=lambda t: -t.cost/t.lives)

    for invest in investments:
        marker = diseases[invest.disease].investment
        if invest.cost < money:
            if marker is None:
                marker = invest
                money -= invest.cost
            elif marker.lives < invest.lives and (money + marker.cost) > invest.cost:
                marker = invest
                money += marker.cost
                money -= invest.cost

    lives = 0
    for disease in diseases:
        if disease.investment is not None:
            lives += disease.investment.lives

    out.write(f"Budget #{budget+1}: Maximum of {lives} lives saved.\n\n")
