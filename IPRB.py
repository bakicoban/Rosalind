def prob(k,m,n):
   total = k + m + n
   return round(( k*(k-1+2*(m+n)) + 0.75*m*(m-1) + m*n ) / ( total*(total-1) ),5)
fh = open("rosalind.txt")
k,m,n = [int(x) for x in fh.readline().strip().split(" ")]

print(prob(k,m,n))
