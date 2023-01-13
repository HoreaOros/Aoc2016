def read():
    lines = open('12.in').read().strip().split('\n')
    prog = []
    for line in lines:
        t = line.split(' ')
        prog.append((t[0], t[1:]))
    return prog

def run(prog, a, b, c, d):
    PC = 0
    while PC >= 0 and PC < len(prog):
        (inst, ops) = prog[PC]
        if inst == 'cpy':
            PC += 1
            value = 0
            if ops[0] in 'abcd':
                if ops[0] == 'a':
                    value = a
                elif ops[0] == 'b':
                    value = b
                elif ops[0] == 'c':
                    value = c
                elif ops[0] == 'd':
                    value = d
            else:
                value = int(ops[0])
            
            if ops[1] == 'a':
                a = value
            elif ops[1] == 'b':
                b = value
            elif ops[1] == 'c':
                c = value
            elif ops[1] == 'd':
                d = value
        elif inst == 'inc':
            PC += 1
            if ops[0] == 'a':
                a += 1
            elif ops[0] == 'b':
                b += 1
            elif ops[0] == 'c':
                c += 1
            elif ops[0] == 'd':
                d += 1
        elif inst == 'dec':
            PC += 1
            if ops[0] == 'a':
                a -= 1
            elif ops[0] == 'b':
                b -= 1
            elif ops[0] == 'c':
                c -= 1
            elif ops[0] == 'd':
                d -= 1
        elif inst == 'jnz':
            offset = int(ops[1])
            if ops[0] == 'a':
                if a != 0:
                    PC += offset
                else:
                    PC += 1
            elif ops[0] == 'b':
                if b != 0:
                    PC += offset
                else:
                    PC += 1
            elif ops[0] == 'c':
                if c != 0:
                    PC += offset
                else:
                    PC += 1
            elif ops[0] == 'd':
                if d != 0:
                    PC += offset
                else:
                    PC += 1
            else:
                if int(ops[0]) != 0:
                    PC += offset
                else:
                    PC += 1
        
    print(a)

prog = read()
run(prog, 0, 0, 0, 0)
run(prog, 0, 0, 1, 0)
