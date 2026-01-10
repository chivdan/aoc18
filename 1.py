def solve(part1: bool):
    result = 0
    deltas = []
    for line in open("input.txt"):
        sign, value = line[:1], int(line[1:].strip())
        deltas.append((1 if sign == "+" else -1) * value)

    if part1:
        print(sum(deltas))
    else:
        freqs = {0}
        while True:
            for delta in deltas:
                result += delta
                if result in freqs:
                    print(result)
                    return
                freqs.add(result)

if __name__ == '__main__':
    solve(True)
    solve(False)

