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
        final = 0
        for number in line.split(" "):
            final += int(number)
        print(final)

level1("level1_2_large.in")