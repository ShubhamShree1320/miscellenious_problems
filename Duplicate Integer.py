class Solution:
    def hasDuplicate(self, nums) -> bool:
        # freq_array=[0]*(max(nums)+1)  ## my solution
        # for i in nums:
        #     freq_array[i]+=1
        # for i in range (len(freq_array)):
        #     if freq_array[i]>1:
        #         return True
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


obj=Solution()
nums = [1, 2, 3, 3]
print(obj.hasDuplicate(nums))

