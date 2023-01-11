
import string
lines = open('6.in').read().strip().split('\n')
#print(lines)

alphabet = list(string.ascii_lowercase)


data = [ {chr(ord('a') + i): 0 for i in range(26)} for _ in range(len(lines[0]))]

for line in lines:
    for i in range(len(line)):
        data[i][line[i]] += 1

r1 = ''
r2 = ''
for i in range(8):
    r1 += max(data[i], key = data[i].get)
    r2 += min(data[i], key = data[i].get)
print(r1)
print(r2)




