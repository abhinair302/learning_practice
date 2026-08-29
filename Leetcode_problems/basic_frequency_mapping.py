# def mapp(nums):
#     freq_map={}
#     for i in range(len(nums)):
#         if nums[i] in freq_map:
#             freq_map[nums[i]]+=1
#         else:
#             freq_map[nums[i]]=1
#     print(freq_map)

# mapp([9,8,2,5,1,1,9,5,2,1])

# Time Complexity=O(n)
# Space Complexity=O(n)




# 2nd Method 

def mapp(nums):
    hash_map={}
    for i in range(len(nums)):
        hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    print(hash_map)

mapp([9,8,2,5,1,1,9,5,2,1])

# Time Complexity=O(n)