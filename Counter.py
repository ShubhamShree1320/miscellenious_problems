from collections import Counter

l=[1,1,2,2,2,2,3,4]

frequency=Counter(l)
print(frequency)
frquency_array=[0]*(max(l)+1)
for k,v in Counter(l).items():
    frquency_array[k]=v
print(frquency_array)


name="shubhamshree"


print(Counter(name).most_common(1)[0][0])