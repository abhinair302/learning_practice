def ls(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i

    return -1

print(ls([5,3,9,8,1,6,4,-10,-100],4))