import heapq

def neighbors(p):
    i, j = p
    return [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]


def dijkstra(start, m):
    q = [(0, start)]
    d = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "#":
                continue
            d[(i, j)] = float('inf')
    d[start] = 0

    while q:
        dist, p = heapq.heappop(q)
        if dist > d[p]:
            continue
        if p != start:
            i, j = p
            if m[i][j] in "EG":
                continue
        for n in neighbors(p):
            if n not in d:
                continue
            i, j = n
            if m[i][j] in "EG":
                continue
            if dist + 1 < d[n]:
                d[n] = dist + 1
                heapq.heappush(q, (dist + 1, n))
    return d


def solve(part1: bool):
    def simulate(elf_damage: int = 3):
        def attack(u, kind, damage):
            candidates = sorted([(units[n][1], n) for n in neighbors(u) if n in units and units[n][0] != kind])
            if len(candidates) == 0:
                return False
            target = candidates[0][1]
            units[target][1] -= damage
            if units[target][1] <= 0:
                units.pop(target)
                m[target[0]][target[1]] = '.'
            return True

        def get_targets(u, kind):
            target_units = [v for v in units if units[v][0] != kind]
            target_squares = []
            for t in target_units:
                for (i, j) in neighbors(t):
                    if m[i][j] == ".":
                        target_squares.append((i, j))
            return target_squares

        def next_step(u, kind):
            target_squares = get_targets(u, kind)
            if not target_squares:
                return None
            d = dijkstra(u, m)
            distances = sorted([(d[t], t) for t in target_squares])
            if distances[0][0] == float('inf'):
                # all targets unreachable
                return None
            dist_to_target, target = distances[0]

            # now calculate distance from the target 
            d = dijkstra(target, m)

            # determine which step to make
            step_options = []
            for (i, j) in neighbors(u):
                if m[i][j] == "." and d[(i, j)] == dist_to_target - 1:
                    step_options.append((i, j))
            return min(step_options)


        damage = {'E': elf_damage,
                  'G': 3}

        m = []
        for line in open("input.txt"):
            m.append([c for c in line.strip()])

        units = {}
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] in "EG":
                    units[(i, j)] = [m[i][j], 200]
        
        n_elves = len([k for k in units if units[k][0] == "E"])

        rounds = 0
        while True:
            if len(set([v[0] for v in units.values()])) == 1:
                # no enemy units left
                break

            # units take turns in reading order
            for u in sorted(units.keys()):
                # unit might already be dead
                if u not in units:
                    continue
                kind, hp = units[u]
                if attack(u, kind, damage[kind]):
                    if not part1 and len([k for k in units if units[k][0] == "E"]) < n_elves:
                        return None

                    if len(set([v[0] for v in units.values()])) == 1:
                        # no enemy units left
                        result = rounds * sum([v[1] for v in units.values()])
                        return result
                    continue

                # determine next step for the unit
                v = next_step(u, kind)

                # if cannot move
                if v is None:
                    continue

                # move unit in dict
                units.pop(u)
                units[v] = [kind, hp]

                # move unit on map
                m[u[0]][u[1]] = "."
                m[v[0]][v[1]] = kind

                # try to attack
                attack(v, kind, damage[kind])

                if not part1 and len([k for k in units if units[k][0] == "E"]) < n_elves:
                    return None

                if len(set([v[0] for v in units.values()])) == 1:
                    # no enemy units left
                    result = rounds * sum([v[1] for v in units.values()])
                    return result
            rounds += 1

        result = rounds * sum([v[1] for v in units.values()])
        return True

    if part1:
        print(simulate(3))
    else:
        damage = 4
        while True:
            result = simulate(damage)
            if result is None:
                damage += 1
            else:
                print(result)
                return

if __name__ == '__main__':
    solve(True) 
    solve(False)
