class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        j=0
        while(j<=x):
            i+=1
            j=i*i
        return i-1

sol=Solution()
print(sol.mySqrt(8))