def lar(nums):
    largest=float("-inf")  #largest=nums[0]
    for i in range(0,len(nums)):
        largest=max(largest,nums[i])
    return largest

print(lar([55,32,-97,99,3,67]))