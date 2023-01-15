import hashlib
input = 'awrkjxxr'
openDoors = 'bcdef'
best = 10000000000
minimPath = ''

maximPath = ''
worst = 0
def walkMin(input, row, col, size, path):
    global best
    global minimPath
    global worst
    global maximPath
    if len(path) > best:
        return best
    if row == size - 1 and col == size - 1:
        if len(path) < best:
            best = len(path)
            minimPath = path
            return best
        else:
            return best
    else:
        hash4 = hashlib.md5((input + path).encode()).hexdigest()[:4]
        # UP
        x = 10000000
        if row > 0 and hash4[0] in openDoors:
            walkMin(input, row - 1, col, size, path + 'U')

        # DOWN
        if row < size -1  and hash4[1] in openDoors:
            walkMin(input, row + 1, col, size, path + 'D')

        # LEFT
        if col > 0 and hash4[2] in openDoors:
            walkMin(input, row, col - 1, size, path + 'L')

        # RIGHT
        if col < size -1  and hash4[3] in openDoors:
            walkMin(input, row, col + 1, size, path + 'R')




def part1(input):
    row = 0
    col = 0
    walkMin(input, row, col, 4, '')
    print(minimPath)


def walkMax(input, row, col, size, path):
    global worst
    global maximPath
    # if len(path) > best:
    #     return best
    if row == size - 1 and col == size - 1:
        if len(path) > worst:
            worst = len(path)
            maximPath = path
            return worst
        else:
            return worst
    else:
        hash4 = hashlib.md5((input + path).encode()).hexdigest()[:4]
        # UP
        x = 10000000
        if row > 0 and hash4[0] in openDoors:
            walkMax(input, row - 1, col, size, path + 'U')

        # DOWN
        if row < size -1  and hash4[1] in openDoors:
            walkMax(input, row + 1, col, size, path + 'D')

        # LEFT
        if col > 0 and hash4[2] in openDoors:
            walkMax(input, row, col - 1, size, path + 'L')

        # RIGHT
        if col < size -1  and hash4[3] in openDoors:
            walkMax(input, row, col + 1, size, path + 'R')


def part2(input):
    row = 0
    col = 0
    walkMax(input, row, col, 4, '')
    print(worst)

part1(input)
part2(input)