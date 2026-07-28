class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n>=2:
            n/=2
        if n==1.0:
            return True
        else:
            return False

sol=Solution()
print(sol.isPowerOfTwo(34))
