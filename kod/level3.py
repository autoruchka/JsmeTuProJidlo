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

        # pos is the integer you already have
        s = 1 if pos > 0 else -1
        a = abs(pos)
        moves = [0]

        if a >= 9:
            # 5,4,3,2, then ones, then 2,3,4,5
            moves += [k * s for k in (5,4,3,2)]
            ones = a - 8
            if ones > 0:
                moves += [1 * s] * ones
            moves += [k * s for k in (2,3,4,5)]

        elif a >= 7:
            # 5,4,3 then 4,5
            moves += [k * s for k in (5,4,3)]
            moves += [k * s for k in (4,5)]

        elif a == 6:
            moves += [k * s for k in (5,4,3,3,4,5)]

        elif a >= 5:
            # 5,4,3 then 4,5
            moves += [k * s for k in (5,4,3)]
            moves += [k * s for k in (4,5)]

        elif a == 4:
            moves += [k * s for k in (5,4,4,5)]

        elif a >= 3:
            moves += [5 * s]

        elif a > 1:
            moves += [5 * s, 5 * s]

        elif a == 1:
            moves += [5 * s]

        moves.append(0)


        moves.append(0)
        output = open(dir.replace("kod", "vystupy") + "/" + level_name.replace(".in", ".out"), "a")
        for i, move in enumerate(moves):
            # skip zeros entirely
            if move == 0:
                continue

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
        output.close()

        if len(moves) >= int(nums[1]):
            print("FAILED")

level1("level3_2_large.in")