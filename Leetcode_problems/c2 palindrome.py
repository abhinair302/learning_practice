# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num=list(str(x))
#         rev_num=[num[rev] for rev in range(len(num)-1,-1,-1)]
#         if (num==rev_num):
#             return True
#         else:
#             return False

# sol=Solution()
# print(sol.isPalindrome(101))




## Optimal Code: 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        result=0
        while (num>0):
            digit=num%10
            result=(result*10)+digit
            num=num//10
        return x==result

sol=Solution()
print(sol.isPalindrome(-101))

# Time Complexity-> O(log base 10 (n))
# Space Complexity-> O(1)
            
