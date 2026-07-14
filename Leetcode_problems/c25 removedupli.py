class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0
        for i in range(1,len(nums)):
            if nums[k]!=nums[i]:
                k+=1
                nums[k]=nums[i]
        return k+1
    
sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))