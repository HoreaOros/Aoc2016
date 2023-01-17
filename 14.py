import hashlib
from collections import deque
import re
salt = 'yjdafjpo'

keys = 64
def getRepeatedHash(str):
    hash = hashlib.md5(str.encode()).hexdigest()
    for _ in range(2016):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def part1():
    index = 0
    count  = 0
    while True:
        while True:
            hash1 = hashlib.md5((salt + str(index)).encode()).hexdigest()

            m = re.search(r'(.)\1{2}', hash1) 
            if  m != None:
                #print(hash1, index)
                break
            index += 1

        (start, _) = m.span()
        c = hash1[start]
        for i in range(1, 1001):
            hash2 = hashlib.md5((salt + str(index + i)).encode()).hexdigest()
            rx = c*5
            m2 = re.search(rx, hash2) 
            if m2 != None:
                count += 1
                print(count, hash1, index)
                print('   ', hash2, index + i)
                break
        if count == keys:
            break
        index += 1
    print(index)



def part2():
    print('Computing repeated hashes...')
    hashes = []
    N = 25000
    for i in range(N):
        hashes.append(getRepeatedHash(salt + str(i)))
    print('Done computing repeated hashes.')
    count = 0
    for index in range(N):
        m = re.search(r'(.)\1{2}', hashes[index]) 
        if  m != None:
            (start, _) = m.span()
            c = hashes[index][start]
            rx = c*5
            for i in range(1, 1001):
                m2 = re.search(rx, hashes[index + i]) 
                if m2 != None:
                    count += 1
                    print('Found key ' + str(count) + ' at index ' + str(index))
                    break
        if count == 64:
            print(index)
            break

#part1()

part2()


