import itertools
fh = open("rosalind.txt")
n = int(fh.readline().strip())
p = list(itertools.permutations(range(n)))
print(len(p))
for i in p:
    for j in i:
        print("{} ".format(j+1), end="")
    print()
