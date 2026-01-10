from functools import cache

def solve(part1: bool):
    claims = []
    for line in open("input.txt"):
        s = line.strip().split()
        claim_id = s[0][1:]
        i, j = [int(v) for v in s[2][:-1].split(",")]
        di, dj = [int(v) for v in s[3].split("x")]
        claims.append((claim_id, i, j, di, dj))

    @cache
    def get_set(claim_id, i, j, di, dj):
        result = set()
        for ii in range(i, i + di):
            for jj in range(j, j + dj):
                result.add((ii, jj))
        return result

    overlap = set()
    intersections = []
    overlapping_ids = set()
    for i in range(len(claims)):
        for j in range(i):
            inter = get_set(*claims[i]).intersection(get_set(*claims[j]))
            if inter:
                intersections.append(inter)
                overlapping_ids.add(i)
                overlapping_ids.add(j)

    if part1:
        for i in intersections:
            overlap = overlap.union(i)
        print(len(overlap))
    else:
        ans = set(range(len(claims))).difference(overlapping_ids)
        print(claims[list(ans)[0]][0])

if __name__ == '__main__':
    solve(True)
    solve(False)

