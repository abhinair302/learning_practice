# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         is_swapped=False
#         n=len(nums)
#         for i in range(n):
#             if nums[i]==0:
#                 for j in range(i+1,n):
#                     if nums[j]!=0:
#                         nums[i],nums[j]=nums[j],nums[i]
#                         i=j
#                         is_swapped=True
#             if is_swapped==False:
#                 break

#         print(nums)

# sol=Solution()
# sol.moveZeroes([1,0,2,4,3,0,0,3,5,1])


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1