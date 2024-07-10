userL = list(map(int, input("list?: ").split()))

max_d = abs(userL[0] - userL[1])
max_idx = 0
i = 1
while i < len(userL)-1:
    if abs(userL[i] - userL[i+1]) > max_d:
        max_d = abs(userL[i] - userL[i+1])
        max_idx = i
    i += 1

print(f'{max_d}({userL[max_idx]}, {userL[max_idx+1]})')