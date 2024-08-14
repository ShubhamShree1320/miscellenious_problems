# I need to sort numbers with frequency
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
from collections import Counter
l=[1,1,2,2,2,2,3,4]
my_count=Counter(l)
print(my_count)
my_sorted=sorted(my_count.items(),key=lambda x:(x[1],x[0]),reverse=False)