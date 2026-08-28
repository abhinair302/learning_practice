class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        digit=1
        while digit>=0 and n>=0 :
            digit=n%10
            sum=sum+(digit**2)
            if sum>=10 and n<10:
                n=sum
                sum=0
                continue
            elif sum<10 and n<10:
                break
            n=n//10
        if sum==1 or sum==7:
            return True
        else:
            return False

sol=Solution()
print(sol.isHappy(1111111))