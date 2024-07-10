def removeMismatched(s: str) -> str: 
    res = []
    braces = 0
    brackets = 0
    paranthesies = 0
    for c in s:
        if c == '(':
            res.append(c)
            paranthesies += 1
        elif c == '[':
            res.append(c)
            brackets += 1
        elif c == '{':
            res.append(c)
            braces += 1
        elif c == ')' and paranthesies > 0:
            res.append(c)
            paranthesies -= 1
        elif c == ']' and brackets > 0:
            res.append(c)
            brackets -= 1
        elif c == '}' and braces > 0:
            res.append(c)
            braces -= 1
    rev = res[::-1]
    for c in rev:
        if paranthesies > 0 and c == '(':
            rev.remove(c)
            paranthesies -=1
        elif brackets > 0 and c == '[':
            rev.remove(c)
            brackets -= 1
        elif braces > 0 and c == '{':
            rev.remove(c)
            braces -= 1

    return ''.join(rev[::-1])


raw = input("Input: ")
final = removeMismatched(raw)
print(final)

