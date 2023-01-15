import re
infile = open('15.in')
lines = infile.read().strip().split('\n')
discs = []
for line in lines:
    m = re.findall(r'\d+', line)
    discs.append((int(m[1]), int(m[3])))
#print(discs)

def solve(discs):
    time = 0
    while True:
        pos = []
        for i in range(len(discs)):
            (total, start) = discs[i]
            pos.append((start + 1 + i + time) % total)
        if all([x == 0 for x in pos]):
            print(time)
            break
        else:
            time += 1

#part1
solve(discs)

#part2
discs.append((11, 0))
solve(discs)
