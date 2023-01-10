lines = open('3.in').read().strip().split('\n')
#print(lines)
count = 0

def genlist(lines):
    r = []
    for line in lines:
        r.append(list(map(int, list(filter(None, line.split(' '))))))
    return r

def isTriangle(a, b, c):
    return (a + b > c and a + c > b and b + c > a)
def part1(list):
    count = 0
    for lst in list:
        (a, b, c) = (lst[0], lst[1], lst[2])
        if isTriangle(a, b, c):
            count += 1
    return count

def part2(list):
    count = 0
    for j in range(3):
        for i in range(len(list) // 3):
            a = list[3 * i][j]
            b = list[3 * i + 1][j]
            c = list[3 * i + 2][j]
            count += 1 if isTriangle(a, b, c) else 0
    return count

lst = genlist(lines)
print(part1(lst))
print(part2(lst))




    