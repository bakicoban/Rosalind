fh = open("rosalind.txt")
n,m = [int(x) for x in fh.readline().strip().split(" ")]

def fib(n, m):
    lis = []
    for i in range(n):
        if i < 2:
            total = 1
            lis.append(total)
        elif (i < m) or (m == 0):
            total = lis[i - 1] + lis[i - 2]
            lis.append(total)
        elif i == m:
            total = lis[i - 1] + lis[i - 2] - 1
            lis.append(total)
        else:
            total = lis[i - 1] + lis[i - 2] - lis[i - (m + 1)]
            lis.append(total)
    return total
print(fib(n,m))
