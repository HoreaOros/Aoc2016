def part1(input):
    lines = open('21.in').read().strip().split('\n')
    passw = list(input)
    #print(lines)
    for line in lines:
        t = line.split(' ')
        # swap position 4 with position 0
        if t[0] == 'swap' and t[1] == 'position':
            i = int(t[2])
            j = int(t[5])
            aux = passw[i]
            passw[i] = passw[j]
            passw[j] = aux
        # swap letter X with letter Y
        elif t[0] == 'swap' and t[1] == 'letter':
            x = t[2]
            y = t[5]
            i = passw.index(x)
            j = passw.index(y)
            aux = passw[i]
            passw[i] = passw[j]
            passw[j] = aux
        # rotate right 6 steps
        elif t[0] == 'rotate' and t[1] == 'right':
            offset = int(t[2])
            for _ in range(offset):
                passw = passw[-1::1] + passw[: len(passw) - 1] 
        # rotate left 4 steps
        elif t[0] == 'rotate' and t[1] == 'left':
            offset = int(t[2])
            for _ in range(offset):
                passw = passw[1:] + passw[0:1] 
        # reverse positions 2 through 7
        elif t[0] == 'reverse':
            x = int(t[2])
            y = int(t[4])
            i = x
            j = y
            while i < j:
                aux = passw[i]
                passw[i] = passw[j]
                passw[j] = aux
                i += 1
                j -= 1
        # move position 7 to position 1
        elif t[0] == 'move':
            x = int(t[2])
            y = int(t[5])
            c = passw[x]
            passw = passw[:x] + passw[x + 1:]
            passw = passw[:y] + list(c) + passw[y:]
        # rotate based on position of letter a
        elif t[0] == 'rotate' and t[1] == 'based':
            c = t[6]
            idx = passw.index(c)
            rot = idx + 1
            if idx >= 4:
                rot += 1
            for _ in range(rot):
                passw = passw[-1::1] + passw[: len(passw) - 1] 

            
    print(''.join(passw))

input = 'abcdefgh'
part1(input)

def part2(input):
    lines = open('21.in').read().strip().split('\n')
    passw = list(input)
    #print(lines)
    lines.reverse()
    for line in lines:
        t = line.split(' ')
        # swap position 4 with position 0
        if t[0] == 'swap' and t[1] == 'position':
            i = int(t[2])
            j = int(t[5])
            aux = passw[i]
            passw[i] = passw[j]
            passw[j] = aux
        # swap letter X with letter Y
        elif t[0] == 'swap' and t[1] == 'letter':
            x = t[2]
            y = t[5]
            i = passw.index(x)
            j = passw.index(y)
            aux = passw[i]
            passw[i] = passw[j]
            passw[j] = aux
        # rotate right 6 steps
        elif t[0] == 'rotate' and t[1] == 'right':
            offset = int(t[2])
            for _ in range(offset):
                passw = passw[1:] + passw[0:1]
        # rotate left 4 steps
        elif t[0] == 'rotate' and t[1] == 'left':
            offset = int(t[2])
            for _ in range(offset):
                passw = passw[-1::1] + passw[: len(passw) - 1] 
        # reverse positions 2 through 7
        elif t[0] == 'reverse':
            x = int(t[2])
            y = int(t[4])
            i = x
            j = y
            while i < j:
                aux = passw[i]
                passw[i] = passw[j]
                passw[j] = aux
                i += 1
                j -= 1
        # move position 7 to position 1
        elif t[0] == 'move':
            x = int(t[5])
            y = int(t[2])
            c = passw[x]
            passw = passw[:x] + passw[x + 1:]
            passw = passw[:y] + list(c) + passw[y:]
        # rotate based on position of letter a
        elif t[0] == 'rotate' and t[1] == 'based':
            c = t[6]
            idx = passw.index(c)
# 0 -> 1             --->>>>>>> 1
# 1 -> 2             --->>>>>>> 3
# 2 -> 3             --->>>>>>> 5
# 3 -> 4             --->>>>>>> 7
# 4 -> 1 + 4 + 1 = 6 --->>>>>>> 2
# 5 -> 1 + 5 + 1 = 7 --->>>>>>> 4
# 6 -> 1 + 6 + 1 = 8 --->>>>>>> 6
# 7 -> 1 + 7 + 1 = 9 --->>>>>>> 0
            if idx == 1:
                rot = 1
            elif idx == 3:
                rot = 2
            elif idx == 5:
                rot = 3
            elif idx == 7:
                rot = 4
            elif idx == 2:
                rot = 6
            elif idx == 4:
                rot = 7
            elif idx == 6:
                rot = 8
            else:
                rot = 9


            for _ in range(rot):
                passw = passw[1:] + passw[:1]


            
    print(''.join(passw))

input = 'fbgdceah'
part2(input)





# rotate based on position of letter d finds the index of letter d (4), 
# then rotates the string right once, 
# plus a number of times equal to that index, 
# plus an additional time because the index was at least 4, 
# for a total of 6 right rotations: decab.

# 0 -> 1             --->>>>>>> 1
# 1 -> 2             --->>>>>>> 3
# 2 -> 3             --->>>>>>> 5
# 3 -> 4             --->>>>>>> 7
# 4 -> 1 + 4 + 1 = 6 --->>>>>>> 2
# 5 -> 1 + 5 + 1 = 7 --->>>>>>> 4
# 6 -> 1 + 6 + 1 = 8 --->>>>>>> 6
# 7 -> 1 + 7 + 1 = 9 --->>>>>>> 0
