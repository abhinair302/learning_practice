# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         k=0
#         for i in range(1,len(nums)):
#             if nums[k]!=nums[i]:
#                 k+=1
#                 nums[k]=nums[i]
#         return k+1
    
# sol=Solution()
# print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         n=len(nums)
#         freq_map={}
#         for i in nums:
#             freq_map[i]=0
#         j=0
#         for i in freq_map:
#             nums[j]=i
#             j+=1
#         return j

    
# sol=Solution()
# print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        i=0
        j=i+1
        while j<n:
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1

sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))