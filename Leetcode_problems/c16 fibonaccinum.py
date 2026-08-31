class Solution:
    def fib(self, n: int) -> int:
        if (n==1 or n==0):
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)

sol=Solution()
print(sol.fib(2))

# def fib(n):
#     if (n==1 or n==0):
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(2))

