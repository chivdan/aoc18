import heapq
from collections import defaultdict

def solve(part1: bool):
    nodes = set()
    parents = defaultdict(set)
    children = defaultdict(set)

    for line in open("input.txt"):
        s = line.strip().split()
        p, c = s[1], s[7]
        nodes.add(p)
        nodes.add(c)
        children[p].add(c)
        parents[c].add(p)

    if part1:
        heap = []
        for n in nodes:
            if not parents[n]:
                heapq.heappush(heap, n)

        result = []
        while heap:
            n = heapq.heappop(heap)
            result.append(n)
            for c in children[n]:
                parents[c].remove(n)
                if not parents[c]:
                    heapq.heappush(heap, c)

        print("".join(result))
    else:
        def T(job):
            return 60 + ord(job) - ord('A') + 1

        heap = []
        for n in nodes:
            if not parents[n]:
                heapq.heappush(heap, n)

        t = 0
        done = set()
        processing = set()
        workers = [(None, 0)] * 5 

        while len(done) < len(nodes):
            # assign new jobs to empty workers, if available
            for i in range(len(workers)):
                job, _ = workers[i]
                if job is None and heap:
                    job = heapq.heappop(heap)
                    workers[i] = (job, T(job))
                    processing.add(job)

            # advance time
            t += 1

            # update workers
            new_workers = []
            for job, remaining_t in workers:
                if job is None:
                    new_workers.append((None, 0))
                    continue
                # reduce job time
                remaining_t -= 1
                if remaining_t == 0:
                    # job is done
                    done.add(job)
                    processing.remove(job)

                    # unlock children of done job
                    for c in children[job]:
                        parents[c].remove(job)
                        if not parents[c]:
                            heapq.heappush(heap, c)

                    new_workers.append((None, 0))
                else:
                    # job is not done
                    new_workers.append((job, remaining_t))

            workers = new_workers

        print(t)


if __name__ == '__main__':
    solve(True) 
    solve(False)

