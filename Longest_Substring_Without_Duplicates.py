def Longest_Substring_Without_Duplicates(s: str) -> int:
    res = 0
    hashset:set = set()
    i = 0
    for j in range(len(s)):
        while s[j] in hashset:
            hashset.remove(s[i])
            i += 1
        hashset.add(s[j])
        res = max(res, j - i + 1)
    return res

s: str = "abcdefghdabcdebb"
print(Longest_Substring_Without_Duplicates(s))
