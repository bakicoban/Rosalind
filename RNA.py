fh = open("rosalind.txt")
s = fh.readline().strip()
s = s.replace("T", "U")
print(s)
