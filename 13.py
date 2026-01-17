import copy

def solve(part1: bool):
    m = []
    for line in open("input.txt"):
        m.append([c for c in line[:-1]])

    def is_cart(c):
        return c in "<>^v"

    def next_pos(i, j, cart):
        if cart == "<":
            return i, j - 1
        elif cart == ">":
            return i, j + 1
        elif cart == "^":
            return i - 1, j
        elif cart == "v":
            return i + 1, j 
        raise Exception()

    carts = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            if is_cart(m[i][j]):
                carts[(i, j)] = [m[i][j], 0]
                if m[i][j] in "^v":
                    m[i][j] = "|"
                else:
                    m[i][j] = "-"

    inter_turns = ["l", "s", "r"]

    turn = {"\\": {">": "v",
                   "^": "<",
                   "v": ">", 
                   "<": "^"},
            "/": {">": "^",
                  "^": ">",
                  "v": "<", 
                  "<": "v"}
            }

    inter = {">": {"l": "^",
                   "s": ">",
                   "r": "v"},
             "v": {"l": ">",
                   "s": "v",
                   "r": "<"},
             "<": {"l": "v",
                   "s": "<",
                   "r": "^"},
             "^": {"l": "<",
                   "s": "^",
                   "r": ">"}
             }


    while True:
        new_carts = {}
        
        if len(carts) <= 1:
            k = list(carts.keys())[0]
            print(f"{k[1]},{k[0]}")
            return

        removed = set()

        for i, j in sorted(carts):
            if (i, j) not in carts:
                continue
            if (i, j) in removed:
                continue
            cart, state = carts.pop((i, j))
            ii, jj = next_pos(i, j, cart)
            if ((ii, jj) in carts or (ii, jj) in new_carts) and (ii, jj) not in removed:
                if part1:
                    print(f"{jj},{ii}")
                    return
                else:
                    removed.add((i, j))
                    removed.add((ii, jj))
                    if (ii, jj) in carts:
                        carts.pop((ii, jj))
                    if (ii, jj) in new_carts: 
                        new_carts.pop((ii, jj))
                    continue
            if m[ii][jj] in "-|":
                pass
            elif m[ii][jj] in "\\/":
                cart = turn[m[ii][jj]][cart]
            elif m[ii][jj] == "+":
                cart = inter[cart][inter_turns[state]]
                state = (state + 1) % 3
            else:
                raise Exception(f"approached {m[ii][jj]} at {ii, jj} from {i, j} with {cart}")

            new_carts[(ii, jj)] = [cart, state]
        
        carts = new_carts


if __name__ == '__main__':
    solve(True)
    solve(False)
