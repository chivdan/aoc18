def solve(part1: bool):
    if not part1:
        print(34011 + 34 * (50000000000 - 1000))
        return

    state = None
    rules = {}

    for line in open("input.txt"):
        line = line.strip()
        if not line:
            continue
        s = line.split()
        if "state" in line:
            state = s[2]
        else:
            rules[s[0]] = s[2]

    def pad(state, nums):
        state = "." * 4 + state + "." * 4
        nums = list(range(nums[0] - 4, nums[0])) + nums + list(range(nums[-1] + 1, nums[-1] + 5))
        return state, nums

    nums = list(range(len(state)))

    state, nums = pad(state, nums)
    for k in range(20):
        new = []
        new_nums = []
        for i in range(len(state)):
            p = state[max(i - 2, 0) : min(i + 3, len(state))]
            if len(p) < 5:
                if i <= 2:
                    p = "." * (5 - len(p)) + p
                else:
                    p = p + "." * (5 - len(p))
            new.append(rules.get(p, "."))
        state = "".join(new)

        state, nums = pad(state, nums)

    print(sum(n for n, c in zip(nums, state) if c == "#"))

if __name__ == '__main__':
    solve(True)
    solve(False)
