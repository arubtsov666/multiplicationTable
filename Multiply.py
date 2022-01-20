dna = input()
g = len(dna)
x = 0
y = 1
z = 1
if dna[x : y] != dna[x + 1: y + 1]:
    print(dna[x:y] + str(z), end="")
for i in range(g):
    if dna[x : y] == dna[x + 1: y + 1]:
        x += 1
        y += 1
        z += 1
        if dna[x : y] != dna[x + 1: y + 1]:
            print(dna[x:y] + str(z), end="")
    else:
        z = 1
        x += 1
        y += 1
        if dna[x: y] != dna[x + 1: y + 1]:
            print(dna[x:y] + str(z), end="")
