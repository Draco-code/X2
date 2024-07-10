name = input("Name: ")
key = input("Key: ")

if "?" in key:
    name_l = []
    key_l = []
    name_l.extend(name)
    key_l.extend(key)
    for idx, c in enumerate(key_l):
        if c == '?':
            key_l[idx] = name_l[idx]

    print("True" if key_l == name_l else "False")
    exit(0)

elif "*" in key: 
    if len(key) == 1:
        print("True")
        exit(0)
    elif key[0] == '*':
        res = name.find(key[1:])
        if res == -1:
            print("False")
            exit(0)
        elif len(name) - res == len(key) -1:
            print("True")
            exit(0)


