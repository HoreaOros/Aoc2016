input = 'cxdnnyjw'
from  hashlib import md5

def part1(input):
    index = 0
    passw = ''
    while len(passw) < 8:
        hash = md5((input + str(index)).encode()).hexdigest()
        if hash[:5] == '00000':
            passw += hash[5]
            print(passw + '.' * (8 - len(passw)))
        index += 1

    print('Part1: ' + passw)

def part2(input):
    print('Part 2...')
    index = 0
    passw = ['_', '_', '_', '_', '_', '_', '_', '_']
    while '_' in passw:
        hash = md5((input + str(index)).encode()).hexdigest()
        if hash[:5] == '00000' and hash[5] in '01234567':
            if passw[int(hash[5])] == '_':
                passw[int(hash[5])] = hash[6]
                print(''.join(passw))
        index += 1
    print('Done.')
#999

part2(input)


