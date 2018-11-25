def fib(n,k):
    lis = [1,1]
    for i in range(2, n):
        lis.append(lis[-2]*k + lis[-1])
    return lis[n-1]

fh = open("rosalind.txt")
n,k = [int(x) for x in fh.readline().strip().split(" ")]
print(fib(n,k))
