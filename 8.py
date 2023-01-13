import numpy as np

lines = open('8.in').read().strip().split('\n')

screen = np.zeros((6, 50), dtype = int)

def part1(lines):
    global screen
    for line in lines:
        t = line.split(' ')
        if len(t) == 2:
            t2 = t[1].split('x')
            A = int(t2[0])
            B = int(t2[1])
            for i in range(B):
                for j in range(A):
                    screen[i, j] = 1
        else:
            offset = int(t[4])
            k = int((t[2].split('='))[1])
            if t[1] == 'row':
                for _ in range(offset):
                    aux = screen[k, 49]
                    for j in range(49, 0, -1):
                        screen[k, j] = screen[k, j - 1]
                    screen[k, 0] = aux
            elif t[1] == 'column':
                for _ in range(offset):
                    aux = screen[5, k]
                    for i in range(5, 0, -1):
                        screen[i, k] = screen[i - 1, k]
                    screen[0, k] = aux
    count  = 0
    for i in range(6):
        for j in range(50):
            if screen[i, j] == 1:
                count += 1
    return count

print(part1(lines))

for i in range(6):
        for j in range(50):
            if j % 5 == 0:
                print(' ', sep = '', end = '' )
            if screen[i, j] == 1:
                print('O', sep = '', end = '')
            else:
                print(' ', sep = '', end = '')
        print()