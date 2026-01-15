def solve():
    points, velocities = [], []
    for line in open("input.txt"):
        line = line.strip().replace("position=", "").replace("velocity=", "").replace("<", "").replace(">", "").replace(",", "")
        x, y, vx, vy = [int(v) for v in line.split()]
        points.append((x, y))
        velocities.append((vx, vy))

    def write_res(points):
        with open(f"output.txt", "w") as f:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    f.write("#" if (x, y) in points else ".")
                f.write("\n")

    min_area = 1e100
    best_points = []
    for i in range(11000):
        points = [(x + dx, y + dy) for (x, y), (dx, dy) in zip(points, velocities)]
        min_x = min(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)
        area = (max_x - min_x) * (max_y - min_y)
        if area < min_area:
            min_area = area
            best_points = points[:]
        else:
            print(i)
            write_res(best_points)
            break


if __name__ == '__main__':
    solve() 
