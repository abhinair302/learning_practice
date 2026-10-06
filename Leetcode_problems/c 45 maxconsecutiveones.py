class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        streak=0
        score=0
        for i in nums:
            if i==1:
                score+=1
            else:
                streak=max(streak,score)
                score=0
            
        return max(streak,score)

sol=Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,0,1,1,1,1,0,1,1]))