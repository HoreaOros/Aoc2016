input = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
rows1 = 40
rows2 = 400000

# Test data: result = 38
#input = '.^^.^.^^^^'
#rows = 10

def solve(input, rows):
    total = input.count('.')
    #print(input)
    for _ in range(rows - 1):
        input = '.' + input + '.'
        new_input = ''
        for i in range(1, len(input) - 1):
            if input[i-1:i + 2] in ['^^.', '.^^', '^..', '..^']:
                new_input += '^'
            else:
                new_input += '.'
        #print(new_input)
        total += new_input.count('.')
        input = new_input
    return total


print(solve(input, rows1))
print(solve(input, rows2))