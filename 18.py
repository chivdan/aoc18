import copy

def solve(part1: bool):
    m = []
    for line in open("input.txt"):
        m.append([c for c in line.strip()])

    def neighbors(i, j):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                if i + di >= len(m):
                    continue
                if j + dj >= len(m[i]):
                    continue
                if i + di < 0 or j + dj < 0:
                    continue
                yield i + di, j + dj

    def neighbor_state(i, j):
        return [m[y][x] for y, x in neighbors(i, j)]
            

    results = []

    N = 10 if part1 else 1000

    for n in range(N):
        m_new = copy.deepcopy(m)
        
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == "." and neighbor_state(i, j).count('|') >= 3:
                    m_new[i][j] = '|'
                elif m[i][j] == '|' and neighbor_state(i, j).count('#') >= 3:
                    m_new[i][j] = '#'
                elif m[i][j] == '#': 
                    if '#' in neighbor_state(i, j) and '|' in neighbor_state(i, j):
                        m_new[i][j] = '#'
                    else:
                        m_new[i][j] = '.'

        m = m_new

        wood, lumber = 0, 0
        for i in range(len(m)):
            wood += m[i].count('|')
            lumber += m[i].count('#')

        results.append(wood * lumber)

    if part1:
        print(results[-1])
    else:
        K = 1000000000
        idx = (K - 1000) % 28
        print(results[idx - 1])


if __name__ == '__main__':
    solve(True)
    solve(False)