#BRUTE-FORCE CODE:

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         max_diff=0
#         diff=0
#         n=len(prices)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if prices[j]>prices[i]:
#                     diff=prices[j]-prices[i]
#                     max_diff=max(max_diff,diff)

#         return max_diff

# sol=Solution()
# print(sol.maxProfit([7,6,4,3,1]))


# OPTIMAL CODE: 

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        min_price=float("inf")
        n=len(prices)
        for i in range(n):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit

sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))