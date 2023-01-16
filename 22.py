import re
lines = open('22.in').read().strip().split('\n')
nodes = []
for line in lines[2:]:
    r = re.findall(r'\d+', line)
    nodes.append((int(r[0]), int(r[1]), int(r[2]), int(r[3]), int(r[4]), int(r[5])))
#print(nodes)
def viable(a, b):
    (x_a, y_a, size_a, used_a, avail_a, use_perc_a) = a
    (x_b, y_b, size_b, used_b, avail_b, use_perc_b) = b
    return used_a != 0 and used_a <= avail_b

count = 0
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j and viable(nodes[i], nodes[j]):
            count += 1

print(count)


maxused = max(nodes, key = lambda x: x[3])
maxavail = max(nodes, key = lambda x: x[4])

print(maxavail)