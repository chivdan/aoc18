def dist(p1, p2):
    i1, j1 = p1
    i2, j2 = p2
    return abs(i1 - i2) + abs(j1 - j2)

def solve(part1: bool):
    points = [tuple([int(v) for v in line.strip().split(", ")]) for line in open("input.txt")]

    min_y = min(p[0] for p in points)
    min_x = min(p[1] for p in points)
    max_y = max(p[0] for p in points)
    max_x = max(p[1] for p in points)

    if part1:
        closest = {n: 0 for n in range(len(points))}
        bad_points = set()
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p1 = y, x
                if p1 in points:
                    continue
                distances = [dist(p1, p2) for p2 in points]
                min_dist = min(distances)
                if distances.count(min_dist) > 1:
                    continue
                else:
                    closest[distances.index(min_dist)] += 1
                    if x == min_x or x == max_x or y == min_y or y == max_y:
                        bad_points.add(points[distances.index(min_dist)])

        max_area = 0
        for n, area in closest.items():
            y, x = points[n]
            if points[n] in bad_points:
                continue
            max_area = max(max_area, area)
        print(max_area + 1)
    else:
        ans = 0
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p1 = y, x
                distances = [dist(p1, p2) for p2 in points]
                if sum(distances) < 10000:
                    ans += 1
        print(ans)
 


if __name__ == '__main__':
    solve(True) 
    solve(False)

