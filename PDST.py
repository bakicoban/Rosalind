#Fasta Parser
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
#distance calculator       
def distance(s1,s2):
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c += 1
    return c/len(s1)

#list of seqquences
seq_list = list(d.values())


for i in seq_list:
    l = []
    for j in seq_list:
        l.append(str(distance(i,j)))
    print(" ".join(l))
