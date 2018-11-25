fh = open("rosalind.txt")
s = fh.readline().strip()
d = {"A":"T", "T":"A", "G":"C", "C":"G"}
s = s[::-1]
ans = ""
for i in s:
    ans += d[i]
print(ans)
