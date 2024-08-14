l=[100,200,101]
Hashset=set(l)
longest=0
for n in Hashset:
    if (n-1) not in Hashset:
        length=1
        while (n+length) in Hashset:
            length+=1
        longest=max(length,longest)
print(longest)