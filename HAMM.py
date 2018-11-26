def hamm(s1,s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
    return c

fh = open("rosalind.txt")
s1 = fh.readline().strip()
s2 = fh.readline().strip()

print(hamm(s1,s2))
