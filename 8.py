def solve(part1: bool):
    s = [int(v) for v in open("input.txt").read().strip().split()]

    def traverse(i: int = 0):
        if i >= len(s):
            return 0, 0
        n_children = s[i]
        n_metadata = s[i + 1]
        j = i + 2
        child_results = []
        for _ in range(n_children):
            j, child_sum = traverse(j)
            child_results.append(child_sum)
        result = 0
        if part1:
            result += sum(child_results)

        if part1 or n_children == 0:
            for k in range(j, j + n_metadata):
                result += s[k]
        elif n_children > 0:
            for k in range(j, j + n_metadata):
                if s[k] == 0:
                    continue
                if s[k] - 1 < n_children:
                    result += child_results[s[k] - 1]

        return j + n_metadata, result

    _, result = traverse()
    print(result)
        

if __name__ == '__main__':
    solve(True) 
    solve(False)

