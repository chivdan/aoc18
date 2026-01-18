def solve(part1: bool):
    N = 503761 if part1 else 1000000
    score = [3, 7]
    pos = [0, 1]

    inp = [5, 0, 3, 7, 6, 1]

    match_pos = 0

    while True:
        s = score[pos[0]] + score[pos[1]]
        L = len(score)
        
        digits = [s // 10, s % 10] if s >= 10 else [s]       
        for d in digits:
            score.append(d)
            if part1 and len(score) == N + 10:
                print("".join([str(c) for c in score[-10:]]))
                return
            elif not part1:
                if match_pos == len(inp):
                    print(len(score) - len(inp) - 1)    
                    return
                if d == inp[match_pos]:
                    match_pos += 1
                elif d == inp[0]:
                    match_pos = 1
                else:
                    match_pos = 0
                            
        for i in range(2):
            pos[i] = (pos[i] + 1 + score[pos[i]]) % len(score)

if __name__ == '__main__':
    solve(True)
    solve(False)
