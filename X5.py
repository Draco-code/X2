with open("c_cod.txt") as cod:
    got = cod.read()
    
print(got + "\n\n")
print(got.replace("+1", "++", got.count("+1")))