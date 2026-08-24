class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        j=0
        while (nums[j]<target and j<len(nums)):
            if j==len(nums)-1:
                break
            j += 1
        if target>nums[j]:
            return nums.index(nums[j])+1

        return nums.index(nums[j])





sol=Solution()
print(sol.searchInsert([1,3,5,6],5))