fh = open("rosalind.txt")
lis = [int(x) for x in fh.readline().strip().split(" ")]
prob = [1, 1, 1, 0.75, 0.5, 0]
c = 0
for i in range(6):
    c += lis[i]*prob[i]
print(c*2)
