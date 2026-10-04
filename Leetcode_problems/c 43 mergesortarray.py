class Solution:
    def findUnion(self, nums1, nums2):
        # code here 
        i,j=0,0
        n,m=len(nums1),len(nums2)
        nums=[]
        while (i<n and j<m):
            if nums1[i]<=nums2[j]:
                if len(nums)==0 or nums1[i]!=nums[-1]:
                    nums.append(nums1[i])
                i+=1
            else:
                if len(nums)==0 or nums2[j]!=nums[-1]:
                    nums.append(nums2[j])
                j+=1
        if i<n:
            while i<n:
                if len(nums)==0 or nums1[i]!=nums[-1]:
                    nums.append(nums1[i])
                i+=1
        if j<m:
            while j<m:
                if len(nums)==0 or nums2[j]!=nums[-1]:
                    nums.append(nums2[j])
                j+=1
        return nums

sol=Solution()
print(sol.findUnion([1,2,3,4,5],[1,2,3]))