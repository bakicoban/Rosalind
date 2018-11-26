map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
comp = {"A":"U", "U":"A", "G":"C", "C":"G"}
def orf(s):
    ls = []
    for i in range(len(s)-2):
        f = False
        pro = ""

        if s[i:i+3] == "AUG":
            for j in range(i, len(s)-2, 3):
                if map[s[j:j+3]] == "STOP":
                    f = True
                    break
                else:
                    pro += map[s[j:j+3]]
        if f == True:
            ls.append(pro)
    return ls


s = input()
s = s.replace("T", "U")
s_comp = ""
for i in s[::-1]:
    s_comp += comp[i]

ans = list(set(orf(s) + orf(s_comp)))
for i in ans:
    print(i)
