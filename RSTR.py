fh = open("rosalind.txt")
N,GC_cont = [float(x) for x in fh.readline().strip().split(" ")]
s = fh.readline().strip()

AT = 0
GC = 0
for i in s:
    if i == 'A' or i == 'T':
        AT += 1
    elif i == 'G' or i == 'C':
        GC += 1
prob_of_s = (((1 - GC_cont) / 2)**AT) * (((GC_cont) / 2)**GC)
prob = 1 - (1 - prob_of_s)**N
print(round(prob,3))
