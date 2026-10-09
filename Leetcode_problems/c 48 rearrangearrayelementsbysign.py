# MY SOLUTION: 
# 
#  class Solution:
#     def rearrangeArray(self, nums: list[int]) -> list[int]:
#         result=[]
#         pos_list=[num for num in nums if num>0]
#         neg_list=[num for num in nums if num<0]
#         for i in range(len(pos_list)):
#             result.append(pos_list[i])
#             result.append(neg_list[i])
#         return result
# sol=Solution()
# print(sol.rearrangeArray(([-1,1])))


# BRUTE FORCE SOLUTION: 

# class Solution:
#     def rearrangeArray(self, nums: list[int]) -> list[int]:
#         result=[]
#         pos_list=[]
#         neg_list=[]
#         for num in nums:    
#             if num>0:
#               pos_list.append(num)
#             else:
#                neg_list.append(num)

#         for i in range(len(pos_list)):
#             result.append(pos_list[i])
#             result.append(neg_list[i])
#         return result
# sol=Solution()
# print(sol.rearrangeArray(([-1,1])))



# OPTIMAL SOLUTION: 

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        posindex,negindex=0,1
        for i in range(n):
            if nums[i]>=0:
                result[posindex]=nums[i]
                posindex+=2
            else:
                result[negindex]=nums[i]
                negindex+=2
        return result

sol=Solution()
print(sol.rearrangeArray([-1,1]))



