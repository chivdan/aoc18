def solve(part1: bool):
    inp = open("input.txt").read().strip().split()
    N = int(inp[0])
    M = int(inp[6])

    if part1:
        s = [0]
        i = 0

        scores = [0] * N
        j = 0

        for m in range(1, M + 1):
            if m % 23 == 0:
                scores[j] += m
                r = (i - 7) % len(s)
                scores[j] += s.pop(r)
                i = r % len(s)
            else:
                i = (i + 2) % len(s)
                s.insert(i, m)

            j = (j + 1) % N
        print(max(scores))
    else:
        M *= 100

        class Node:
            def __init__(self, num):
                self.num = num
                self.next = None
                self.prev = None

        def insert_after(node, new_node):
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            new_node.prev = node

        def remove(node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def get_prev(node, steps):
            result = node
            for _ in range(steps):
                result = result.prev
            return result
        
        node = Node(0)
        node.next = node 
        node.prev = node

        scores = [0] * N
        j = 0

        for m in range(1, M + 1):
            if m % 23 == 0:
                scores[j] += m
                node = get_prev(node, 7)
                nxt = node.next
                scores[j] += node.num
                remove(node)
                node = nxt
            else:
                n = Node(m)
                node = node.next
                insert_after(node, n)
                node = n

            j = (j + 1) % N
        print(max(scores))

if __name__ == '__main__':
    solve(True) 
    solve(False)
