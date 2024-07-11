
group_b = {}

with open ('workersInfo.txt') as rawInfo:
    base = rawInfo.read().split('\n')

for i, line in enumerate(base): # just to split and convert bonus to int
    base[i] = line.split()
    base[i][-2] = int(base[i][-2])

for group in list(map(lambda x : x[-1], base)): # creating dict with group names as keys
    if not group in group_b.keys():
        group_b[group] = 0

for line in base: # calculating scores
    _, _, _, bonus, group = line
    if bonus > 0:
        group_b[group] += 1
    elif bonus < 0:
        group_b[group] -= 1
print(group_b)
best_score = max(group_b.values())

for gr, val in group_b.items(): #printing groups with highest score
    if val == best_score:
        print(gr)
