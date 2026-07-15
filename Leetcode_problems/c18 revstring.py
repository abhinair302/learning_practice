# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         for i in range(len(s)-1,-1,-1):
#             s.append(s.pop(i))
#         print(s)

# sol=Solution()
# sol.reverseString(["h","e","l","l","o"])

# class Solution:

#     def reverseString(self, s: list[str]) -> None:
#         for i in range(len(s)//2):
#             temp=s[i]
#             s[i]=s[len(s)-i-1]
#             s[len(s)-i-1]=temp
         
#         print(s)

# sol=Solution()
# sol.reverseString(["H","a","n","n","a","h"])

class Solution:

    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1;right-=1
         
        print(s)

sol=Solution()
sol.reverseString(["H","a","n","n","a","h"])