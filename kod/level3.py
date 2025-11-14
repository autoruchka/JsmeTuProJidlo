import os

def level1(level_name):
    # gives the path of demo.py
    path = os.path.realpath(__file__)

    # gives the directory where demo.py
    # exists
    dir = os.path.dirname(path)
    file = open(dir.replace("kod", "vstupy") + "/" + level_name, "r")
    i = 0
    for line in file:
        if i == 0:
            i += 1
            continue
        new_line = line.rsplit()
        final = [0]
        nums = line.split(" ")
        pos = int(nums[0])

        moves = [0]

        if abs(pos) >= 9: 
            for i in range(-5, -1):
                moves.append(i * -(pos / abs(pos)))
            ones = abs(pos) - 8
            for i in range(0, ones):
                moves.append(1 * (pos / abs(pos)))
            for i in range(2, 6):
                moves.append(i * (pos / abs(pos)))
        elif abs(pos) >= 7:
            for i in range(-5, -2):
                moves.append(i * (pos / abs(pos)))
            for i in range(4, 6):
                moves.append(i * (pos / abs(pos)))
        elif abs(pos) >= 5:
            for i in range(-5, -2):
                moves.append(i * -(pos / abs(pos)))
            for i in range(4, 6):
                moves.append(i * (pos / abs(pos)))
        elif abs(pos) >= 3:
            for i in range(-5, -3):
                moves.append(i * -(pos / abs(pos)))
            moves.append(5 * (pos / abs(pos)))
        elif abs(pos) > 1:
            moves.append(5 * (pos / abs(pos)))
            moves.append(5 * (pos / abs(pos)))
        elif abs(pos) == 1:
            moves.append(5 * (pos / abs(pos)))

        moves.append(0)
        output = open(dir.replace("kod", "vystupy") + "/" + level_name.replace(".in", ".out"), "a")
        for move in moves:
            output.write(str(int(move)) + " ")
        output.write("\n")
        output.close()

level1("level3_2_large.in")