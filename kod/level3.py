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
        smth = line.split(" ")
        nums = smth[0].split(",")
        pos = int(nums[0])
        posY = int(nums[1])

        moves = [0]

        # pos is the integer you already have
        s = 1 if pos > 0 else -1
        a = abs(pos)

        if a >= 9:
            # 5,4,3,2, then ones, then 2,3,4,5
            moves += [k * s for k in (5,4,3,2)]
            ones = a - 8
            if ones > 0:
                moves += [1 * s] * ones
            moves += [k * s for k in (2,3,4,5)]
        elif a == 8:
            moves += [k * s for k in (5,4,3,2)]
            moves += [k * s for k in (2,3,4,5)]
        elif a >= 7:
            # 5,4,3 then 4,5
            moves += [k * s for k in (5,4,3,2)]
            moves += [k * s for k in (3,4,5)]

        elif a == 6:
            moves += [k * s for k in (5,4,3,3,4,5)]

        elif a >= 5:
            # 5,4,3 then 4,5
            moves += [k * s for k in (5,4,3)]
            moves += [k * s for k in (4,5)]

        elif a == 4:
            moves += [k * s for k in (5,4,4,5)]

        elif a >= 3:
            moves += [5 * s, 4 * s, 5 * s]

        elif a > 1:
            moves += [5 * s, 5 * s]

        elif a == 1:
            moves += [5 * s]

        moves.append(0)

        # pos is the integer you already have
        sY = 1 if posY > 0 else -1
        aY = abs(posY)
        movesY = [0]

        if aY >= 9:
            # 5,4,3,2, then ones, then 2,3,4,5
            movesY += [kY * sY for kY in (5,4,3,2)]
            onesY = aY - 8
            if onesY > 0:
                movesY += [1 * sY] * onesY
            movesY += [kY * sY for kY in (2,3,4,5)]
        elif aY == 8:
            movesY += [kY * sY for kY in (5,4,3,2)]
            movesY += [kY * sY for kY in (2,3,4,5)]
        elif aY >= 7:
            # 5,4,3 then 4,5
            movesY += [kY * sY for kY in (5,4,3,2)]
            movesY += [kY * sY for kY in (3,4,5)]

        elif aY == 6:
            movesY += [kY * sY for kY in (5,4,3,3,4,5)]

        elif aY >= 5:
            # 5,4,3 then 4,5
            movesY += [kY * sY for kY in (5,4,3)]
            movesY += [kY * sY for kY in (4,5)]

        elif aY == 4:
            movesY += [kY * sY for kY in (5,4,4,5)]

        elif aY >= 3:
            movesY += [5 * sY, 4 * sY, 5 * sY]

        elif aY > 1:
            movesY += [5 * sY, 5 * sY]

        elif aY == 1:
            movesY += [5 * sY]

        movesY.append(0)

        output = open(dir.replace("kod", "vystupy") + "/" + level_name.replace(".in", ".out"), "a")
        for i, move in enumerate(moves):

            # get neighbors
            prev = moves[i - 1] if i > 0 else None
            nxt  = moves[i + 1] if i < len(moves) - 1 else None

            # check previous
            if prev is not None and prev != 0:
                if (move > 0) != (prev > 0):
                    print("FAILED")

            # check next
            if nxt is not None and nxt != 0:
                if (move > 0) != (nxt > 0):
                    print("FAILED")

            output.write(str(int(move)) + " ")
        output.write("\n")
        for i, move in enumerate(movesY):
            prev = movesY[i - 1] if i > 0 else None
            nxt  = movesY[i + 1] if i < len(movesY) - 1 else None

            # check previous
            if prev is not None and prev != 0:
                if (move > 0) != (prev > 0):
                    print("FAILED")

            # check next
            if nxt is not None and nxt != 0:
                if (move > 0) != (nxt > 0):
                    print("FAILED")

            output.write(str(int(move)) + " ")
        output.write("\n")
        output.write("\n")
        output.close()

        if len(moves) >= int(nums[1]):
            print("FAILED")

level1("level4_2_large.in")