import math
# lines = open('23.in').read().strip().split('\n')
# reg = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

# prog = []
# for line in lines:
#     t = line.split(' ')
#     prog.append((t[0], t[1:]))

# PC = 0
# while PC >= 0 and PC < len(prog):
#     #print(PC, sep = ' ', end = '')
#     if prog[PC][0] == 'inc':
#         reg[prog[PC][1][0]] += 1
#         PC += 1
#     elif prog[PC][0] == 'dec':
#         reg[prog[PC][1][0]] -= 1
#         PC += 1
#     elif prog[PC][0] == 'cpy':
#         if prog[PC][1][1] in reg: # doar daca destinatia e reg se poate executa CPY
#             if prog[PC][1][0] in reg:
#                 reg[prog[PC][1][1]] = reg[prog[PC][1][0]]
#             else:
#                 reg[prog[PC][1][1]] = int(prog[PC][1][0])
#         PC += 1
#     elif prog[PC][0] == 'jnz':
#         if prog[PC][1][1] in reg:
#             offset = reg[prog[PC][1][1]]
#         else:
#             offset = int(prog[PC][1][1])

#         if prog[PC][1][0] in reg:
#             value = reg[prog[PC][1][0]]
#         else:
#             value = int(prog[PC][1][0])
#         if value != 0:
#             PC += offset
#         else:
#             PC += 1
#     elif prog[PC][0] == 'tgl':
#         if prog[PC][1][0] in reg:
#             offset = reg[prog[PC][1][0]]
#         else:
#             offset = int(prog[PC][1][0])
#         if PC + offset >= 0 and PC + offset < len(prog):
#             if len(prog[PC + offset][1]) == 1:
#                 if prog[PC + offset][0] == 'inc':
#                     prog[PC + offset] = ('dec', prog[PC + offset][1])
#                 else:
#                     prog[PC + offset] = ('inc', prog[PC + offset][1])
#             elif len(prog[PC + offset][1]) == 2:
#                 if prog[PC + offset][0] == 'jnz':
#                     prog[PC + offset] = ('cpy', prog[PC + offset][1])
#                 else:
#                     prog[PC + offset] = ('jnz', prog[PC + offset][1])
#         PC += 1

# print(reg['a'])
print(math.factorial(12) + 6160)


