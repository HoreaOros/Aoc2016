inst = open('1.in').read().strip().split(', ')
print(inst)

row = 0
col = 0
dir = {'N':{'R':'E', 'L':'W'}, 
       'E':{'R':'S', 'L': 'N'}, 
       'S':{'R':'W', 'L': 'E'},
       'W':{'R':'N', 'L': 'S'}}
curr = 'N'
SEEN = {(0, 0)}
p2found = False

for  c in inst:
    k = c[0]
    delta = int(c[1:])
    curr = dir[curr][k]
    if curr =='N':
        if not p2found:
            for i in range(1, delta + 1):
                if (row - i, col) in SEEN:
                    p2found = True
                    p2row = row - i
                    p2col = col
                    break
                else:
                    SEEN.add((row - i, col))
        row -= delta

    elif curr == 'S':
        if not p2found:
            for i in range(1, delta + 1):
                if (row + i, col) in SEEN:
                    p2found = True
                    p2row = row + i
                    p2col = col
                    break
                else:
                    SEEN.add((row + i, col))
        row += delta
    elif curr == 'E':
        if not p2found:
            for i in range(1, delta + 1):
                if (row, col + i) in SEEN:
                    p2found = True
                    p2row = row
                    p2col = col + i
                    break
                else:
                    SEEN.add((row, col + i))
        col += delta
    else:
        if not p2found:
            for i in range(1, delta + 1):
                if (row, col - i) in SEEN:
                    p2found = True
                    p2row = row
                    p2col = col - i
                    break
                else:
                    SEEN.add((row, col - i))
        col -= delta
    
    



print(abs(row) + abs(col))
print(abs(p2row) + abs(p2col))