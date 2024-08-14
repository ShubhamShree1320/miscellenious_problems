def binary_search(arr,target):
    arr.sort()
    l=0
    u=len(arr)-1
    while l<=u:
        mid=l+(u-l)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            l=mid+1
        else:
            u=mid-1
    return False





nums = [-1,0,2,4,6,8]
target = 4
print(binary_search(nums,target))
