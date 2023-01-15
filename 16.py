input = '10010000000110000'
diskLen1 = 272
diskLen2 = 35651584
def b(input):
    reverse = input[::-1]
    ch = []
    for c in reverse:
        if c == '0':
            ch.append('1')
        else:
            ch.append('0')
    return ''.join(ch)

def part1(input, diskLen):
    while len(input) < diskLen:
        #print(input)
        input = input + '0' + b(input)
    
    data = input[:diskLen]

    checksum = ''
    while diskLen % 2 == 0:
        checksum = ''
        for i in range(0, diskLen, 2):
            if data[i] == data[i + 1]:
                checksum += '1'
            else:
                checksum += '0'
        diskLen = diskLen // 2
        data = checksum
    print(checksum)


        


part1(input, diskLen1)
part1(input, diskLen2)
