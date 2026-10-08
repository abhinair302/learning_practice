# My solution: TLE ERROR

# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         n=len(nums)
#         highest_score=float("-inf")
#         for i in range(0,n):
#             score=0
#             for j in range(i,n):
#                 score=score+nums[j]
#                 highest_score=max(highest_score,score)
#         return highest_score

# sol=Solution()
# print(sol.maxSubArray([-2,-1])) 





# OPTIMAL SOLUTION

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        highest_score=float("-inf")
        score=0
        for i in range(0,n):
            score=score+nums[i]
            highest_score=max(highest_score,score)
            if score<0:
                score=0
        return highest_score

sol=Solution()
print(sol.maxSubArray([-2,-1])) 