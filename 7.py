import re
lines = open('7.in').read().strip().split('\n')

def containsABBA(s):
    for i in range(len(s) - 3):
        if (s[i] != s[i + 1]) and (s[i] == s[i + 3] and s[i + 1] == s[i + 2]):
            return True
    return False

def getABAs(s):
    aba = []
    for i in range(len(s) - 2):
        if (s[i] != s[i + 1]) and (s[i] == s[i + 2]):
            aba.append(s[i:i + 3])
    return aba

def supportTLS(line):
    t = re.split('\[|\]', line)
    outside = False
    inside = False
    for i in range(len(t)):
        if containsABBA(t[i]):
            if i % 2 == 0:
                outside = True
            else:
                inside = True
    return outside and not inside

def supportSSL(line):
    t = re.split('\[|\]', line)
    supernet = []
    hypernet = []
    for i in range(len(t)):
        if i % 2 == 0:
            supernet.append(t[i])
        else:
            hypernet.append(t[i])
    for item in supernet:
        abas = getABAs(item)
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            for x in hypernet:
                if x.count(bab) > 0:
                    return True
    
    return False


##########################
part1 = 0
part2 = 0
for line in lines:
    if supportTLS(line):
        part1 += 1
    if supportSSL(line):
        part2 += 1

print(part1)
print(part2)
