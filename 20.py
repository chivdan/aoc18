import heapq

def dijkstra(start, g):
    q = [(0, start)]
    d = {v: float('inf') for v in g}
    d[start] = 0

    while q:
        dist, p = heapq.heappop(q)
        if dist > d[p]:
            continue
        i, j = p
        for n in g[p]:
            if n not in d:
                continue
            i, j = n
            if dist + 1 < d[n]:
                d[n] = dist + 1
                heapq.heappush(q, (dist + 1, n))
    return d


def solve(part1: bool):
    def step(i, j, d):
        if d == "N":
            return i - 1, j
        elif d == "S":
            return i + 1, j
        elif d == "E":
            return i, j + 1
        elif d == "W":
            return i, j - 1

    def draw_map(i, j, r, pos):
        start = i, j
        while True:
            if pos >= len(r):
                return pos
            if r[pos] in "NEWS":
                c = r[pos]
                ni, nj = step(i, j, c)
                g.setdefault((i, j), set()).add((ni, nj))
                g.setdefault((ni, nj), set()).add((i, j))
                i, j = ni, nj
                pos += 1
            elif r[pos] == "(":
                pos = draw_map(i, j, r, pos + 1)
            elif r[pos] == "|":
                i, j = start
                pos += 1
            elif r[pos] == ")":
                return pos + 1

    g = {(0, 0): set()}
    r = open("input.txt").read().strip()[1:-1]
    pos = draw_map(0, 0, r, 0)
    
    d = dijkstra((0, 0), g)
    if part1:
        max_dist = 0
        for v in g:
            if d[v] == float('inf'):
                continue
            max_dist = max(d[v], max_dist)

        print(max_dist)
    else:
        n_1000 = 0
        for v in g:
            if d[v] == float('inf'):
                continue
            elif d[v] >= 1000:
                n_1000 += 1
        print(n_1000)
 

    
if __name__ == '__main__':
    solve(True) 
    solve(False)
