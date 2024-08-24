s = "racecar" # r=2,c=2,a=2,e=2
t = "carracy" ## r=2,c=2,a=2,e=2

from collections import Counter
# def creating_char_int_array(string):
#     char_array= [ char for char in string]
#     int_array=[int(ord(char)+ord('a')) for char in char_array]
#     return int_array

# int_array_s=creating_char_int_array(s)
# int_array_t=creating_char_int_array(t)

# int_array_t=sorted(int_array_t)
# int_array_s=sorted(int_array_s)
# are_equal = int_array_t == int_array_s

s_freq=Counter(s)
t_freq=Counter(t)
d=[0]*26
p=[0]*26
for k,v in s_freq.items():
    d[int(ord(k)-ord('a'))]=v
for k,v in t_freq.items():
    d[int(ord(k)-ord('a'))]=v
are_equal=d.sort()==p.sort()
print(are_equal)