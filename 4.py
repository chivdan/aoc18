def solve(part1: bool):
    guards = {}

    guard = None
    start = None
    for line in open("sorted.txt"):
        s = line.strip().split()
        date = s[0][1:]
        minutes = int(s[1].split(":")[1][:-1])
        if "begins shift" in line:
            guard = int(s[3][1:])
            if guard not in guards:
                guards[guard] = {}
        elif "asleep" in line:
            start = minutes
        elif "wakes up" in line:
            if date not in guards[guard]:
                guards[guard][date] = []
            guards[guard][date].extend(list(range(start, minutes)))

    if part1:
        sleepy_guard = None
        max_sleep = 0
        for g in guards:
            sleep = sum(len(guards[g][d]) for d in guards[g])
            if sleep > max_sleep:
                max_sleep = sleep
                sleepy_guard = g

        # minute most frequently asleep
        minutes = []
        for d, m in guards[sleepy_guard].items():
            minutes.extend(m)

        sleepy_minute = max(minutes, key=lambda m: minutes.count(m))
        print(sleepy_guard * sleepy_minute)
    else:
        max_minute_asleep = None
        sleepy_guard = None
        ntimes_asleep = 0
        for g in guards:
            # minute most frequently asleep
            minutes = []
            for d, m in guards[g].items():
                minutes.extend(m)
            if not minutes:
                continue

            sleepy_minute = max(minutes, key=lambda m: minutes.count(m))
            count = minutes.count(sleepy_minute)
            if count > ntimes_asleep:
                ntimes_asleep = count
                max_minute_asleep = sleepy_minute
                sleepy_guard = g

        print(sleepy_guard * max_minute_asleep)
            

if __name__ == '__main__':
    solve(True)
    solve(False)

