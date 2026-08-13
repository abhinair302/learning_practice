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

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            