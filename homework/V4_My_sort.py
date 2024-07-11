def sumUnits(n: int) -> int:
    ln = len(str(n))
    sum = 0

    while ln:
        sum += n%10
        n /= 10
        ln -= 1

    return sum

def mySort(l: list) -> list:
    return sorted(l, key= lambda x: sumUnits(x))

ord = [14, 56, 30, 103]
final = mySort(ord)
print(final)