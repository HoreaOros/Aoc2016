lines = open('20.in').read().strip().split('\n')
r = []
#4294967296
for line in lines:
    t = line.split('-')
    r.append( (int(t[0]), int(t[1])))

r = sorted(r, key = lambda x: x[0])

#print(r)

def inside(a, b):
    return a[0] >= b[0] and a[1] <= b[1]

def part1(r):
    i = 0
    while True:
        j = i + 1
        while inside(r[j], r[i]):
            j = j + 1
        if r[i][1] + 1 < r[j][0]:
            print(r[i][1] + 1)
            break
        else:
            i = j


part1(r)

def part2(r):
    i = 0
    total = 0
    while i < len(r):
        j = i + 1
        while j < len(r) and inside(r[j], r[i]):
            j = j + 1
        if j < len(r) and r[i][1] + 1 < r[j][0]:
            total += r[j][0] - r[i][1] - 1
        i = j
    maxright = max(r, key = lambda x:x[1])
    print(maxright)
    return total
print(part2(r))