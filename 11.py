from collections import deque
from copy import deepcopy
N = 5
E = 1
elements = ['Pr', 'Co', 'Cu', 'Ru', 'Pl']
data = [
    {'G': ['Pr'], 'M': ['Pr']},
    {'G': ['Co', 'Cu', 'Ru', 'Pl'], 'M': []},
    {'G': [], 'M': ['Co', 'Cu', 'Ru', 'Pl']}, 
    {'G': [], 'M': []}]

def checkFloor(floor): # primeste argument un dictionar
    if floor['G'] == []: # daca nu este nici un generator e OK
        return True
    if floor['M'] == []: # daca nu este nici un microchip e OK
        return True
    
    # daca toate microchipurile au generatorul corespunzator e OK
    for elem in floor['M']:
        if not elem in floor['G']:
            return False
    return True





def tipar(data):
    for i in range(4, 0, -1):
        print('F' + str(i) + ' ', sep = ' ', end = '')
        if i == E:
            e = 'E '
        else:
            e = '. '
        print(e, sep = ' ', end = '')
        s = ''
        for item in elements:
            if item in data[i - 1]['G']:
                s = s + item + 'G' + ' '
            else:
                s = s + ' . '+ ' '
            if item in data[i - 1]['M']:
                s = s + item + 'M' + ' '
            else:
                s = s + ' . '+ ' '
        print(s)
    print('=' * 45)

# for x in data:
#     print(checkFloor(x))

# reuniune a doua dictionare
def union(curr, d):
    return {'G': curr['G'] + d['G'], 'M': curr['M'] + d['M']}


# diferenta a doua dictionare
def difference(curr, d):
    r = {'G': [], 'M': []}
    for g in curr['G']:
        if not g in d['G']:
            r['G'].append(g)
    for m in curr['M']:
        if not m in d['M']:
            r['M'].append(m)
    
    return r
# hash the state (because dict and list is not hashable)
def myHash(state):
    (E, data, depth) = state
    return (E, str(data), depth)

print(str(data))

Q = deque()
best = 100000000000
state = (E, deepcopy(data), 0)
Q.append(state)

SEEN = set()

while Q:
    state = Q.popleft()
    (E, data, depth) = state
    tipar(data)
    if myHash(state) in SEEN:
        continue

    SEEN.add((E, str(data), depth))   
  
    if E == 4 and len(data[E - 1]['G']) == N and len(data[E - 1]['M']) == N:
        if depth <= best:
            best = depth
            print(best)
        continue
    
    if depth >= best:
        continue

    floor = deepcopy(data[E - 1])

    # creez o lista cu toate combinatiile de iteme ce pot fi scoase (fara sa le scot efectiv)
    # vor fi scoase doar daca combinatia poate fi dusa la etajul E-1 sau E+1
    p = []

    # scot cate un chip
    for m in floor['M']:
        d = {'G': [], 'M': []}
        d['M'].append(m)
        p.append(d)
    # scot cate doua chipuri
    if len(floor['M']) >= 2:
        for m1 in floor['M']:
            for m2 in floor['M']:
                if m1 != m2:
                    d = {'G': [], 'M': []}
                    d['M'].append(m1)
                    d['M'].append(m2)
                    p.append(d)
    # scot un generator (doar daca pot sa il scot)
    if len(floor['G']) >= 1:
        for g in floor['G']:
            if not g in floor['M']:
                d = {'G': [], 'M': []}
                d['G'].append(g)
                p.append(d)
    # scot doua generatoare (doar daca pot sa le scot)
    if len(floor['G']) >= 2:
        for g1 in floor['G']:
            if not g1 in floor['M']:
                for g2 in floor['G']:
                    if not g2 in floor['M']:
                        if g1 != g2:
                           d = {'G': [], 'M': []}
                           d['G'].append(g1)
                           d['G'].append(g2)
                           p.append(d) 
    
    # scot un generator si un chip (doar daca le pot scoate si daca am cel putin un G si un M)
    if len(floor['G']) >= 1 and len(floor['M']) >= 1:
        for g in floor['G']:
            for m in floor['M']:
                d = {'G': [], 'M': []}
                if g == m or not g in floor['M']:
                    d['G'].append(g)
                    d['M'].append(m)
                    p.append(d)
    
    # aici am in lista p toate combinatiile de a scoate G si M de pe pe etajul E
    # pentru fiecare combinatie verific daca poate fi trimisa pe etajul E + 1
    # pentru fiecare combinatie verific daca poate fi trimisa pe etajul E - 1
    for d in p:
        if E < 4:
            newdata = deepcopy(data)
            currentfloor = deepcopy(newdata[E - 1])
            upfloor = deepcopy(newdata[E])

            newfloor = union(upfloor, d)
            if checkFloor(newfloor):
                newdata[E] = newfloor
                newdata[E - 1] = difference(currentfloor, d)
                Q.append((E + 1, newdata, depth + 1))
        if E > 1:
            #optimizari
            if E == 2 and data[0]['G'] == [] and data[0]['M'] == []:
                continue
            if E == 3 and data[0]['G'] == [] and data[0]['M'] == [] and data[1]['G'] == [] and data[1]['M'] == []:
                continue
            newdata = deepcopy(data)
            currentfloor = deepcopy(newdata[E - 1])
            downfloor = deepcopy(data[E - 2])

            newfloor = union(downfloor, d)
            if checkFloor(newfloor):
                newdata[E - 2] = newfloor
                newdata[E - 1] = difference(currentfloor, d)
                Q.append((E - 1, newdata, depth + 1))
                    
    
print(best)


