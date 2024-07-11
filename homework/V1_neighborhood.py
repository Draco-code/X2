def neighbors(lst: list) -> list:
    result = []
    for idx in range(len(lst) -1):
        if lst[idx] * lst[idx+1] > 0:
            result.append([lst[idx], lst[idx+1]])
    return result

mylist = list(map(int, input("Input: ").split()))
save = neighbors(mylist)

for i in save:
    print(i)