naqsh = input("Naqsh: ").split()
# naqsh = ['Red', 'Yellow', 'Green', 'Green']
# print(naqsh)
time = 2

for i, c in enumerate(naqsh[1:]):
    time += 2
    if not c == naqsh[i]:
        time += 1

print(time)