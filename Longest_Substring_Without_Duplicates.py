def Longest_Substring_Without_Duplicates(s):
    res=0
    hashset=set()
    for i in range(len(s)):
        if s[i] not in hashset:
            hashset.add(s[i])
            res=max(res,len(hashset))
    return res

s="abcdefghdabcdebb"
print(Longest_Substring_Without_Duplicates(s))