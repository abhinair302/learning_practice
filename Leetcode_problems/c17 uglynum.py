class Solution:
    def isUgly(self, n: int) -> bool:
        if (n<=0):
            return False
        while n%2==0:
            n=n/2
        while n%3==0:
            n=n/3
        while n%5==0:
            n=n/5
        if int(n)==1 or int(n)==2 or int(n)==3 or int(n)==5:
            return True
        else:
            return False
sol=Solution()
print(sol.isUgly(8))