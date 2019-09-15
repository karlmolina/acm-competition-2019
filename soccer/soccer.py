file = open('soccer.in')

num = int(file.readline())

out = open('soccer.out', 'w')


class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.scored = 0
        self.allowed = 0

    def __repr__(self):
        return self.name


for group in range(num):
    line = file.readline().split(' ')
    # print(line)
    teams = int(line[0])
    games = int(line[1])

    line = file.readline().strip().split(' ')
    dict = {team: Team(team) for team in line}
    # print(dict.keys())

    for game in range(games):
        gameline = file.readline().strip().split(' ')
        team1 = gameline[0]
        points1 = int(gameline[1])
        team2 = gameline[2]
        points2 = int(gameline[3])

        dict[team1].scored += points1
        dict[team1].allowed += points2
        dict[team2].scored += points2
        dict[team2].allowed += points1

        if points1 > points2:
            dict[team1].wins += 1
            dict[team2].losses += 1
        elif points2 > points1:
            dict[team2].wins += 1
            dict[team1].losses += 1
        else:
            dict[team1].draws += 1
            dict[team2].draws += 1

    out.write(f"Group {group+1}:\n")

    sortteam = sorted(dict.values(), key=lambda t: t.name)
    # print(sortteam)
    sortteam = sorted(sortteam, key=lambda t: -t.scored)
    # print(sortteam)
    sortteam = sorted(sortteam, key=lambda t: t.allowed - t.scored)
    # print(sortteam)
    sortteam = sorted(sortteam, key=lambda t: -(3 * t.wins + t.draws))

    # print(sortteam)

    for team in sortteam:
        out.write(
            f"{team.name} {3* team.wins + team.draws} {team.wins} {team.losses} {team.draws} {team.scored} {team.allowed}\n")

    out.write('\n')