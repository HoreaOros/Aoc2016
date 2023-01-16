elfs = 3014387
#elfs = 16
def part1(elfs):
    c_elfs = elfs
    p = [ 1 for _ in range(elfs)]

    i = 0
    while elfs > 1:
        while p[i] == 0:
            i = (i + 1) % c_elfs
        
        result = i
        i = (i + 1) % c_elfs
        while p[i] == 0:
            i = (i + 1) % c_elfs
        p[i] = 0
        elfs -= 1
    return result + 1


#print(part1(elfs))

def part2(elfs):
    c_elfs = elfs
    p = [ x for x in range(1,elfs + 1)]
    i = 0
    
    while len(p) > 1:
        if len(p) % 1000 == 0:
            print(len(p))
        p.pop((i + elfs // 2) % elfs)

        elfs -= 1
        if i == elfs:
            i == 0
        else:    
            i = (i + 1) % elfs

        #print(p)

    return p[0]
print(part2(elfs))