fh = open("rosalind.txt")
s = fh.readline().strip()
lis = ["A", "C", "G", "T"]
newlis = []
for i in lis:
    newlis.append(str(s.count(i)))
print(" ".join(newlis))
