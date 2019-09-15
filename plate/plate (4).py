file = open('plate.in')

acts = int(file.readline())

out = open('plate.out', 'w')


class Plate:
    def __init__(self, velocity, time):
        self.time = time
        self.velocity = velocity



for act in range(acts):
    line = file.readline().strip().split(' ')
    poles = int(line[0])
    speed = int(line[1])
    out.write(f"Circus Act {act+1}:\n")

    plates = [speed for i in range(poles)]

    time = 0
    for i in range(-1, len(plates)):
        plates[i] = -5 * time + speed
        time += 0.5

    if(plates[-1] < 0 and len(plates) != 1):
        out.write("Chester will fail!\n")
    else:
        out.write("Chester can do it!\n")

    # if poles == 1:
    #     out.write("Chester can do it!\n")
    # elif (speed / 5 < (poles) / 2):
    #     out.write("Chester will fail!\n")
    # else:
    #     out.write("Chester can do it!\n")

    out.write("\n")
