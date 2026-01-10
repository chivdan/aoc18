def react(m):
    start = 0
    while True:
        changed = False
        for i in range(start, len(m) - 1):
            if abs(ord(m[i]) - ord(m[i + 1])) == 32:
                m = m[:i] + m[i + 2:]
                changed = True
                start = max(0, i - 1)
                break
        if not changed:
            break
    return m


def solve(part1: bool):
    m = open("input.txt").read().strip()           

    if part1:
        print(len(react(m)))
    else:
        min_length = 1e10
        for i in range(ord("a"), ord("z") + 1):
            c = chr(i)
            C = c.upper()
            s = m.replace(c, "").replace(C, "")
            reduced = react(s)
            min_length = min(min_length, len(reduced))
        print(min_length)

if __name__ == '__main__':
    solve(True)
    solve(False)

