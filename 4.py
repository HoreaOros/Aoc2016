from itertools import groupby

lines = open('4.in').read().split('\n')
#print(lines)
result = 0
for line in lines:
    t = line.split('-')
    #id, checksum
    t2 = t[-1][:-1].split('[')
    id = int(t2[0])
    checksum = t2[1]
    # name
    name = ''.join(t[:-1])
    rotate = ''
    for c in name:
        i = (ord(c) - ord('a') + id % 26) % 26
        rotate += chr(ord('a') + i)
    #print(rotate, id)
    if 'north' in rotate:
        print('Part 2 answer:', id)
    
    name = sorted(name)
    it = groupby(name, lambda x: x)
    lst = []
    for key, group in it:
        lst.append((key, len(list(group))))
    lst = sorted(lst, key = lambda x: x[1], reverse=True)


    cs = ''.join([x[0] for x in lst[:5]])
    if cs == checksum:
        result += id

print('Part 1 answer:', result)

