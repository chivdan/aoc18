import heapq
from functools import cache

def solve(part1: bool):
    depth = 3879
    start = 0, 0
    target = 8, 713

    @cache
    def erosion_level(x, y):
        return (depth + geoindex(x, y)) % 20183

    @cache
    def geoindex(x, y):
        if x == 0 and y == 0:
            return 0
        if x == target[0] and y == target[1]: 
            return 0
        if y == 0:
            return x * 16807
        if x == 0:
            return y * 48271
        return erosion_level(x - 1, y) * erosion_level(x, y - 1)

    @cache
    def region_type(x, y):
        el = erosion_level(x, y) % 3
        return el % 3
        

    def neighbors(x, y):
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


    reg_type = ["rocky", "wet", "narrow"]
    #torch = 0; gear = 1
    tools = {"rocky": [0, 1],
             "wet": [1, -1],
             "narrow": [0, -1]}

    if part1:
        result = 0
        for x in range(target[0] + 1):
            for y in range(target[1] + 1):
                result += region_type(x, y)
        print(result)
        return

    q = [(0, start, 0)]
    d = {(start, 0): 0}

    while q:
        cost, node, cur_tool = heapq.heappop(q)

        cur_region = reg_type[region_type(*node)]
        if cur_tool not in tools[cur_region]:
            continue

        if (node, cur_tool) == (target, 0):
            print(cost)
            return

        if cost > d.get((node, cur_tool), float('inf')):
            continue

        for n in neighbors(*node):
            if n[0] < 0 or n[1] < 0:
                continue
            allowed_tools = tools[reg_type[region_type(*n)]]
            if cur_tool in allowed_tools:
                n_cost = cost + 1
                state = (n, cur_tool)
                if n_cost < d.get(state, float('inf')):
                    d[state] = n_cost
                    heapq.heappush(q, (n_cost, n, cur_tool)) 


        allowed_tools = tools[reg_type[region_type(*node)]]
        for tool in allowed_tools:
            if tool == cur_tool:
                continue
            n_cost = cost + 7  
            state = (node, tool)
            if n_cost < d.get(state, float('inf')):
                d[state] = n_cost
                heapq.heappush(q, (n_cost, node, tool)) 

if __name__ == '__main__':
    solve(True)
    solve(False)
