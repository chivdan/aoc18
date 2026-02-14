import copy

def solve(part1: bool):
    def select_targets(attackers, defenders):
        targets = []
        sorted_attackers = sorted(attackers, key=lambda g: (g['n'] * g['damage'], g['initiative']), reverse=True) 
        for attacker in sorted_attackers:
            if attacker['n'] <= 0:
                targets.append(None)
                continue
            damage_type = attacker['damage_type']
            non_immune = [d for d in defenders if d is not None and d['n'] > 0 and d not in targets and damage_type not in d['immune']]
            if not non_immune:
                targets.append(None)
                continue

            effective_power = attacker['n'] * attacker['damage']
            
            if True:
                non_immune = [(effective_power * 2 if damage_type in g['weak'] else effective_power, g) for g in non_immune]
                non_immune.sort(key=lambda ni: (ni[0], ni[1]['n'] * ni[1]['damage']), reverse=True)
                highest_damage = non_immune[0][0]
                highest_power = non_immune[0][1]['n'] * non_immune[0][1]['damage']

                good_targets = [
                    (g['initiative'], g)
                    for (dam, g) in non_immune
                    if dam == highest_damage and g['n'] * g['damage'] == highest_power
                ]

                good_targets.sort(reverse=True)
                targets.append(good_targets[0][1])

            if False:
                candidates = []
                for g in defenders:
                    if g['n'] <= 0:
                        continue
                    if g in targets:
                        continue
                    if damage_type in g['immune']:
                        continue
        
                    damage = effective_power * 2 if damage_type in g['weak'] else effective_power
                    if damage == 0:
                        continue
                    candidates.append((damage, 
                                       g['n'] * g['damage'],
                                       g['initiative'],
                                       g))

                if not candidates:
                    targets.append(None)
                    continue

                candidates.sort(reverse=True)
                targets.append(candidates[0][-1])            
        return list(zip(sorted_attackers, targets))
        

    teams = {}
    team_name = None

    for line in open("input.txt"):
        line = line.strip()
        if ":" in line:
            team_name = line[:-1]
            teams[team_name] = []
        elif "units" in line:
            group = {}

            s = line.split()
            group['n'] = int(s[0])
            group['hp'] = int(s[4])
            group['damage'] = int(s[s.index("does") + 1])
            group['damage_type'] = s[s.index("does") + 2]
            group['initiative'] = int(s[-1])
            group['weak'] = []
            group['immune'] = []

            if "(" in line:    
                weak_immune = line[line.index("(") + 1: line.index(")")]
                if ";" in weak_immune:
                    parts = weak_immune.split(";")
                else:
                    parts = [weak_immune]

                for p in parts:
                    for prop in ["weak", "immune"]:
                        if prop in p:
                            p = p.replace(prop + " to ", "")
                            p = p.strip().split(",")
                            group[prop] = [v.strip() for v in p]
            teams[team_name].append(group)

    original_teams = copy.deepcopy(teams)
    
    def fight(boost: int):
        for g in teams['Immune System']:
            g['damage'] += boost

        while True:
            total_before = sum(g['n'] for team in teams.values() for g in team)
            
            # target selection
            immune_system = teams["Immune System"]
            infection = teams["Infection"]
        
            if any(sum(g['n'] for g in team) == 0 for team in teams.values()):
                break
            
            targets = []
            targets += select_targets(immune_system, infection)
            targets += select_targets(infection, immune_system)
            targets.sort(key=lambda p: p[0]['initiative'], reverse=True)
            for attacker, defender in targets:
                if attacker['n'] == 0:
                    continue
                if defender is None:
                    continue
                if defender['n'] == 0:
                    continue
                damage_type = attacker['damage_type']
                effective_power = attacker['n'] * attacker['damage']
                damage = effective_power * 2 if damage_type in defender['weak'] else effective_power
                hp = defender['hp']
                units_killed = damage // hp
                if units_killed > defender['n']:
                    units_killed = defender['n']

                defender['n'] -= units_killed

            total_after = sum(g['n'] for team in teams.values() for g in team)
            if total_before == total_after:
                break        
        return teams
        
    if part1:
        fight(0)
        print(sum(sum(g['n'] for g in team) for team in teams.values()))
    else:
        boost = 1
        while True:
            teams = copy.deepcopy(original_teams)
            fight(boost)
            if all(g['n'] == 0 for g in teams['Immune System']):
                boost += 1
                continue
            elif all(g['n'] == 0 for g in teams['Infection']):
                print(sum(g['n'] for g in teams['Immune System']))
                break
            else:
                boost += 1
                continue
            
        

if __name__ == '__main__':
    solve(True)
    solve(False)
