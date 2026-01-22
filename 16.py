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

    def count(before, op, after):
        return sum([foo(before, *op[1:]) == after for foo in ops])

    result = 0
    examples = []
    program = []
    before, op, after = None, None, None
    for line in open("input.txt"):
        line = line.strip()
        if "Before" in line:
            before = line.split(" ", 1)[1].strip()[1:-1]
            before = [int(v) for v in before.split(", ")]
        elif "After" in line:
            after = line.split(" ", 1)[1].strip()[1:-1]
            after = [int(v) for v in after.split(", ")]
            examples.append((before, op, after))
            before, op, after = None, None, None
        elif before is not None and after is None:
            op = [int(v) for v in line.strip().split()]
        elif line:
            program.append([int(v) for v in line.split()])
    
    if part1:
        print(sum(count(before, op, after) >= 3 for (before, op, after) in examples))
    else:
        opcode_examples = {o: [] for o in range(len(ops))}
        for before, op, after in examples:
            opcode_examples[op[0]].append((before, op[1:], after))
    
        def search(known, opcode):
            children = []
            for foo in ops:
                if foo in known.values():
                    continue
                if all(foo(before, *args) == after for before, args, after in opcode_examples[opcode]):
                    child = copy.copy(known)
                    child[opcode] = foo
                    children.append(search(child, opcode + 1))
            if not children:
                return known
            return max(children, key=lambda d: len(d))
    
        opcode_map = search({}, 0)

        reg = [0, 0, 0, 0]
        for op, a, b, c in program:
            reg = opcode_map[op](reg, a, b, c)

        print(reg[0])


if __name__ == '__main__':
    solve(True) 
    solve(False)
