def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('rosalind.txt') as fp:
    d = {}
    for name, seq in read_fasta(fp):
        d[name] = seq


a = [0]*len(list(d.values())[0])
c = [0]*len(list(d.values())[0])
g = [0]*len(list(d.values())[0])
t = [0]*len(list(d.values())[0])

for i in list(d.values()):
    for j in range(len(list(d.values())[0])):
        if i[j] == "A":
            a[j] += 1
        elif i[j] == "C":
            c[j] += 1
        elif i[j] == "G":
            g[j] += 1
        elif i[j] == "T":
            t[j] += 1


ans = ""
for i in range(len(a)):
    if a[i] == max(a[i], c[i], t[i], g[i]):
        ans += "A"
    elif c[i] == max(a[i], c[i], t[i], g[i]):
        ans += "C"
    elif t[i] == max(a[i], c[i], t[i], g[i]):
        ans += "T"
    elif g[i] == max(a[i], c[i], t[i], g[i]):
        ans += "G"
print(ans)
print("A: " + " ".join([str(x) for x in a]))
print("C: " + " ".join([str(x) for x in c]))
print("G: " + " ".join([str(x) for x in g]))
print("T: " + " ".join([str(x) for x in t]))
