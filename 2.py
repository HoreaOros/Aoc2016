lines = open('2.in').read().strip().split('\n')

def part1():
    keypad = [[1,2,3], [4,5,6], [7,8,9]]
    keys = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
            4: (1, 0), 5: (1, 1), 6: (1, 2), 
            7: (2, 0), 8: (2, 1), 9: (2, 2)}
    (row, col) = keys[5]
    r = ''
    for line in lines:
        for i in line:
            if i == 'U' and row > 0:
                row -= 1
            if i == 'D' and row < 2:
                row += 1
            if i == 'R' and col < 2:
                col += 1
            if i == 'L' and col > 0:
                col -= 1
        r = r + str(keypad[row][col])
    return r
print(part1())
    
def part2():
    keypad = {'1': {'D': '3'},
              '2': {'D': '6', 'R': '3'}, 
              '3': {'U': '1', 'D': '7', 'L': '2', 'R': '4'}, 
              '4': {'D': '8', 'L': '3'},
              '5': {'R': '6'},
              '6': {'U': '2', 'D': 'A', 'L': '5', 'R': '7'},
              '7': {'U': '3', 'D': 'B', 'L': '6', 'R': '8'},
              '8': {'U': '4', 'D': 'C', 'L': '7', 'R': '9'},
              '9': {'L': '8'},
              'A': {'U': '6', 'R': 'B'},
              'B': {'U': '7', 'D': 'D', 'L': 'A', 'R': 'C'},
              'C': {'U': '8', 'L': 'B'},
              'D': {'U': 'B'}}
    k = '5'
    r = ''
    for line in lines:
        for c in line:
            if c in keypad[k]:
                k = keypad[k][c]
        r = r + k
    return r
print(part2())
