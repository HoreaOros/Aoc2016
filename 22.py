import re
import numpy as np
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


def part1():
    count = 0
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j and viable(nodes[i], nodes[j]):
                count += 1

    print(count)


#part1()



# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     89T   65T    24T   73%

def part2():
    print(len(nodes))
    rows = 29
    cols = 35
    # map = np.zeros((rows, cols), dtype='U5')
    # for node in nodes:
    #     if node[3] == 0:
    #         v = ' _/' + str(node[2])
    #     elif node[3] < 10:
    #         v = ' ' + str(node[3]) + '/' + str(node[2])
    #     elif node[3] < 100:
    #         v = str(node[3]) + '/' + str(node[2])
    #     else:
    #         v = '|' + '/' + str(node[2])
    #     map[node[1], node[0]] = v

    # outfile = open('22.out', 'w')
    # for i in range(rows):
    #     outfile.write(' '.join(map[i]))
    #     outfile.write('\n')
    # outfile.close()

    map2 = np.zeros((rows, cols), dtype='U1')
    for node in nodes:
        if node[3] == 0:
            map2[node[1], node[0]] = '_'
        elif node[3] < 100:
            map2[node[1], node[0]] = '.'
        else:
            map2[node[1], node[0]] = '#'

    outfile = open('22.out', 'w')
    for i in range(rows):
        outfile.write(' '.join(map2[i]))
        outfile.write('\n')
    outfile.close()
part2()