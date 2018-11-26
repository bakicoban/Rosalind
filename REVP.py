s = input()
comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
for i in range(4,13):
    for j in range(len(s)-i+1):
        seq = s[j:i+j]
        seqrev = ""
        for k in seq[::-1]:
            seqrev += comp[k]
        if seq == seqrev:
            print(j+1, i)
