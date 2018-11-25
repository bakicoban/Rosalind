def fasta_reader(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def GC_calc(s):
    c = 0
    for i in s:
        if i == "G" or i == "C":
            c += 1
    res = round((c/len(s))*100,6)
    return res

with open('rosalind.txt') as fp:
    d = {}
    for name, seq in fasta_reader(fp):
        d[name[1:]] = seq

newd = {}
for i in d:
    newd[i] = GC_calc(d[i])
print(max(newd, key=newd.get))
print(newd[max(newd, key=newd.get)])
