# Brute Force Solution: 

# def factors(n):
#     result=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             result.append(i)
#     return result

# print(factors(36))

#   Time Complexity: O(n)
#   Space Complexity: O(k)




# Better Solution: 

# def factors(n):
#     result=[]
#     for i in range(1,(n//2)+1):
#         if n%i==0:
#             result.append(i)
#     result.append(n)
#     return result

# print(factors(36))

#   Time Complexity: O(n/2)= O(N)
#   Space Complexity: O(k)




# Optimal Solution: 

from math import *

def factors(n):
    result=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if n//i!=i:
                result.append(n//i)
    result.sort()
    return result

print(factors(36))

# Time Complexity: O(n log n)+O(sqrt(n))
# Space Complexity: O(k)