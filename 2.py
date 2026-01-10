def solve(part1: bool):
    twos, threes = 0, 0
    lines = [line.strip() for line in open("input.txt")]
    if part1:
        for line in lines:
            if any(line.count(c) == 3 for c in set(line)):
                threes += 1
            if any(line.count(c) == 2 for c in set(line)):
                twos += 1

        print(twos * threes)
    else:
        for i in range(len(lines)):
            for j in range(i):
                diff = sum(ci != cj for ci, cj in zip(lines[i], lines[j]))
                if diff == 1:
                    common = [ci if ci == cj else "" for ci, cj in zip(lines[i], lines[j])]
                    print("".join(common))
                    return

if __name__ == '__main__':
    solve(True)
    solve(False)

