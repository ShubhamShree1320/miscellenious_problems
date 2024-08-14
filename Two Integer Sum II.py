def Two_Integer_SumII(nums, target):
    l,r=0,len(nums)-1
    while l<r:
        if nums[l]+nums[r]==target:
            return [l+1,r+1]
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            r-=1

numbers = [1,2,3,4]
target = 3

print(Two_Integer_SumII(numbers,target))


