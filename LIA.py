import math
fh = open("rosalind.txt")
k,N = [int(x) for x in fh.readline().strip().split(" ")]
P = 2**k
probability = 0
for i in range(N, P + 1):
    prob = (math.factorial(P) / (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(P - i))
    probability += prob
print(round(probability,3))
