## Optimal Code: 

class Solution:
    def isArmstrong(self, n: int) -> bool:
        num=n
        total=0
        nod=len(str(n))
        while (num>0):
            total=total+((num%10)**nod)
            num=num//10
        return (n==total)            

sol=Solution()
print(sol.isArmstrong(153))

# Time Complexity-> O(log base 10 (n))
# Space Complexity-> O(1)