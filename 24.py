import numpy as np
from itertools import combinations
from collections import deque

lines = open('24.in').read().strip().split('\n')
SITES = 8

rows = len(lines)
cols = len(lines[0])
map = np.zeros((rows, cols), dtype=str)
for i in range(rows):
    for j in range(cols):
        map[i, j] = lines[i][j]


sites = [() for i in range(SITES)]
for i in range(rows):
    for j in range(cols):
        if map[i, j].isdigit():
            sites[int(map[i, j])] = (i, j)

def Lee(map, start, stop):
    Q = deque()
    
    VISITED = set()
    SEEN = set()
    Q.append((start, 0))
    VISITED.add(start)
    while Q:
        state = Q.popleft()
        (node, depth) = state

        if node == stop:
            return depth

        dr = [0, 0, 1, -1]
        dc = [-1, 1, 0, 0]
        (row, col) = node
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            new_node = (new_row, new_col)
            if map[new_row, new_col] != '#' and not new_node in VISITED:
                VISITED.add(new_node)
                new_state = (new_node, depth + 1)
                Q.append(new_state)
            
        

##############
## Generare matrice adiacenta
adj = np.zeros((SITES, SITES), dtype = int)
for i in range(SITES):
    for j in range(i):
        r = Lee(map, sites[i], sites[j])
        adj[i, j] = adj[j, i] = r
##############

# tiparire matrice adiacenta
# for i in range(SITES):
#     for j in range(SITES):
#         print(adj[i, j], sep = '', end = '')
#         print(' ', end = '')
#     print()


# implement HELD-KARP algorithm
g = dict()
for k in range(1, SITES):
    g[(frozenset([k]), k)] = adj[0, k]

for s in range(2, SITES):
    for S in combinations([x for x in range(1, SITES)], s):
        for k in S: 
            minim = 1000000000
            for m in S:
                if m != k:
                    diff = set(S) - set([k])
                    value = g[(frozenset(diff), m)] + adj[m, k]
                    if value < minim:
                        minim = value
            g[(frozenset(S), k)] = minim

def part1():
    minim = 10000000000
    s = frozenset([x for x in range(1, SITES)])
    for k in range(1, SITES):
        if g[(s,k)] < minim:
            minim = g[(s,k)]
    print(minim)

def part2():
    minim = 10000000000
    s = frozenset([x for x in range(1, SITES)])
    for k in range(1, SITES):
        if g[(s,k)] + adj[0, k] < minim:
            minim = g[(s,k)] + adj[0, k]
    print(minim)


part1()
part2()




