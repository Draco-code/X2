def mostVote(D: dict) -> list:
    ones = 0
    zeros = 0

    for v in D.values():
        if v == 1:
            ones += 1
        elif v == 0:
            zeros += 1

    return [1, 0] if ones == zeros else [1] if ones > zeros else [0]
    

source = {
    'Anvar': 1, 
    'Lobar': 1, 
    'Asror': 0, 
    'Vali': 0, 
    'Surayyo': 1, 
    'Baxtiyor': 1
}

for mv in mostVote(source):
    print('\n', mv)
    for key, val in source.items():
        if val == mv:
            print(key, end = ' ')