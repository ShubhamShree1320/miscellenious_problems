def three_sum(nums,target):
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            if nums[i]+nums[l]+nums[r]==target:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif nums[i]+nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1
    return res


nums = [-1,0,1,2,-1,-4]
target = 0

print(three_sum(nums,target))