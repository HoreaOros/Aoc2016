import re
markerRE = '\(\d*x\d*\)'

input = open('9.in').read().strip()

def part1(input):
    result = ''
    
    while len(input) > 0:
        m = re.search(markerRE, input)
        if m != None:
            (start, end) = m.span()
            
            # daca start > 0 copiez in result caractere de la inceput pana la primul marker
            if start > 0:
                result += input[:start]

            
            marker = input[start:end]
            marker = marker[1:-1]
            t = marker.split('x')
            count = int(t[0])
            times = int(t[1])

            input = input[end:]

            repeat = input[:count]
            input = input[count:]

            result += repeat * times
        else:
            result += input
            break
    return result

print(len(part1(input)))

def part2(input):
    if len(input) > 0:
        m = re.search(markerRE, input)
        if m != None:
            (start, end) = m.span()
            if start > 0:
                return start + part2(input[end:])
            else:
                marker = input[start:end]
                marker = marker[1:-1]
                t = marker.split('x')
                count = int(t[0])
                times = int(t[1])
                
                r = part2(input[end:end+count])

                return r * times + part2(input[end+count:])
                

        else:
            return len(input)
    else:
        return 0



print(part2(input))
