from collections import deque

input = 1362
steps = 50
start_x = 1 
start_y = 1 

target_x = 31
target_y = 39

def wall(x, y):
    r = x*x + 3*x + 2*x*y + y + y*y + input
    ones = 0
    while r != 0:
        if r % 2 == 1:
            ones += 1
        r //= 2
    return ones % 2 == 1




count = 0
Q = deque()
Q.append((start_x, start_y, count))
SEEN = set()
VISITED = set()
dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]
part1 = False
while Q:
    state = Q.popleft()
    (x, y, c) = state
    
    SEEN.add(state)
    VISITED.add((x, y))
    
    if not part1 and x == target_x and y == target_y:
        print(c)
        part1 = True
        #break
    
    # part2 
    if c == steps:
        #print(len(SEEN))
        continue

    # toti vecinii nevazuti ai lui x, y ii adaug in coada
    for i in range(len(dx)):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x >= 0 and new_y >= 0 and not wall(new_x, new_y):
            new_state = (new_x, new_y, c + 1)
            if not (new_x, new_y) in VISITED:
                Q.append(new_state)


print(len(VISITED))