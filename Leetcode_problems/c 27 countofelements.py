# Counting Integers between 0 and 10: 

# def count_ele(m,n):
#     hash_list=[0,0,0,0,0,0,0,0,0,0,0]
#     for num in m:
#         hash_list[num]+=1

#     for num in n:
#         if num>0 and num<=10:
#             print(num,":",hash_list[num])
#         else:
#             print(num,":",0)

# count_ele([5,3,2,2,1,5,5,7,5,10],[10,111,1,9,5,67,2])

# Time Complexity: O(m+n)
# Space Complexity: O(10)=O(1)



# Counting Characters of Strings consisting of only small letters:

# def count_ele(s,q):
#     hash_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#     for ch in s:
#         asci=ord(ch)
#         index=asci-97
#         hash_list[index]+=1
#     for ch in q:
#         asci=ord(ch)
#         index=asci-97
#         print(ch,":",hash_list[index])


# count_ele("azyxyyzaaaa",["d","a","y","x"])

# Time Complexity: O(m+n)
# Space Complexity: O(26)=O(1)


def count_ele(s,q):
    hash_list={}
    for n in range(len(s)):
        hash_list[s[n]]=hash_list.get(s[n],0)+1
    for ch in q:
        if ch in hash_list:
            print(ch,":",hash_list[ch])
        else:
            print(ch,":",0)

count_ele("azyxyyzaaaa",["d","a","y","x"])