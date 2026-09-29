def check(nums):
    n=len(nums)
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            return False
    return True

print(check([2,3,4,67,2,6,9]))
print(check([1,2,3,4,5]))


def check(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True

print(check([2,3,4,67,2,6,9]))
print(check([1,2,3,4,5]))

