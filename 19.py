import copy

def addr(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] + reg[b]
    return res

def addi(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] + b
    return res

def mulr(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] * reg[b]
    return res

def muli(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] * b
    return res

def banr(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] & reg[b]
    return res

def bani(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] & b
    return res

def borr(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] | reg[b]
    return res

def bori(reg, a, b, c):
    res = reg[:]
    res[c] = reg[a] | b
    return res

def setr(reg, a, b, c):
    res = reg[:]
    res[c] = res[a]
    return res

def seti(reg, a, b, c):
    res = reg[:]
    res[c] = a
    return res

def gtir(reg, a, b, c):
    res = reg[:]
    res[c] = int(a > reg[b])
    return res

def gtri(reg, a, b, c):
    res = reg[:]
    res[c] = int(reg[a] > b)
    return res

def gtrr(reg, a, b, c):
    res = reg[:]
    res[c] = int(reg[a] > reg[b])
    return res

def eqir(reg, a, b, c):
    res = reg[:]
    res[c] = int(a == reg[b])
    return res

def eqri(reg, a, b, c):
    res = reg[:]
    res[c] = int(reg[a] == b)
    return res

def eqrr(reg, a, b, c):
    res = reg[:]
    res[c] = int(reg[a] == reg[b])
    return res


def solve(part1: bool):
    ops = [addr, addi, mulr, muli, banr, bani,
           borr, bori, setr, seti, gtir, gtri, gtrr,
           eqir, eqri, eqrr]
    ops_map = {foo.__name__: foo for foo in ops}

    ip_reg = None

    program = []
    for line in open("input.txt"):
        line = line.strip()
        s = line.split()
        if "#ip" in line:
            ip_reg = int(s[1])
        else:
            program.append([s[0]] + [int(v) for v in s[1:]])

    reg = [0] * 6

    if not part1:
        #reg[0] = 1
        ans = 0
        x = 10551329
        ans = sum(i for i in range(1, x + 1) if x % i == 0)
        print(ans)
        return

    i = 0
    while True:
        if i < 0 or i >= len(program):
            break
        reg[ip_reg] = i
        op, a, b, c = program[i]
        reg = ops_map[op](reg, a, b, c)
        #print(i, program[i], reg)
        i = reg[ip_reg] + 1

    print(reg[0])


   
    
if __name__ == '__main__':
    solve(True) 
    solve(False)
