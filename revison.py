# def merge(left, right):
#     res = []
#     l = 0
#     r = 0
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             res.append(left[l])
#             l += 1
#         else:
#             res.append(right[r])
#             r += 1
#     while l < len(left):
#         res.append(left[l])
#         l += 1
#     while r < len(right):
#         res.append(right[r])
#         r += 1

#     return res

# def merge_sort(arr, l, u):
#     if l >= u:
#         return [arr[l]]
#     m = l + ((u - l) // 2)
#     left_sorted = merge_sort(arr, l, m)
#     right_sorted = merge_sort(arr, m + 1, u)
#     return merge(left_sorted, right_sorted)

# def quick_sort(array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot=array[-1]
#         left=[x for x in array[:-1] if x<=pivot]
#         right=[x for x in array[:-1] if x>pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr = [1, 2, 4, 3,0]
# # print(f"Merge Sort = {merge_sort(arr, 0, len(arr) - 1)}")
# print(f"Quick = {quick_sort(arr)}")

# class Encode_Decode:
#     def encode(self,str_list):
#         res=''
#         for s in str_list:
#             res+=str(len(s))+'#'+s
#         return res
#     def decode(self,value):
#         res,i=[],0
#         while i < len(value):
#             j=i
#             if value[j]!='#':
#                 j+=1
#             length=int(value[i:j])
#             res.append(value[j+1:j+1+length])
#             i=j+1+length
#         return res




# l=["Hello","Boy"]
# obj=Encode_Decode()
# print(obj.decode(obj.encode(l)))

# def longest_substring_no_dup(s: str) -> int:
#     hashset: set = set()
#     length = 0
#     i = 0  # Start pointer for the current substring
#     for j in range(len(s)):  # End pointer for the current substring
#         while s[j] in hashset:
#             hashset.remove(s[i])
#             i += 1
#         hashset.add(s[j])
#         length = max(length, j - i + 1)
#     return length

# s: str = "abcc"
# print(longest_substring_no_dup(s))  # Output should be 3, for "abc"


n: list[int] = [1, 2, 3, 4]

# Initialize prefix and postfix arrays with 1s
pre_mul: list[int] = [1] * len(n)
post_mul: list[int] = [1] * len(n)
res: list[int] = [1] * len(n)

# Calculate the prefix products
for i in range(1, len(n)):
    pre_mul[i] = pre_mul[i - 1] * n[i - 1]

# Calculate the postfix products
for i in range(len(n) - 2, -1, -1):  # Start from second last element and go backwards
    post_mul[i] = post_mul[i + 1] * n[i + 1]

# Combine the prefix and postfix products to get the result
for i in range(len(n)):
    res[i] = pre_mul[i] * post_mul[i]

print("Prefix Multiplication:", pre_mul)
print("Postfix Multiplication:", post_mul)
print("Result:", res)
