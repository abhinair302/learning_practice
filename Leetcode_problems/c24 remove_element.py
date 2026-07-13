# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         k=0
#         for element in nums:
#             if element==val:
#                 nums.remove(element)
#                 nums.append('_')
#             else:
#                 k+=1
#         return k

# sol=Solution()
# print(sol.removeElement([3,2,2,3],3))

# The above program was the one which I had tried, but was not correct







# Then, after understanding the correct pattern from the solution, I was able to finally solve this, given below..      


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k=0
        for position in range(len(nums)):
            if nums[position]!=val:
                nums[k]=nums[position]
                k+=1
        return k

sol=Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2],2))      