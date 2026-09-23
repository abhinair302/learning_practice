def partition(arr,low,high):
    pivot=arr[low]
    i,j=low,high
    while (i<j):
        while (pivot>=arr[i] and i<=high-1):
            i+=1
        while (pivot<arr[j] and j>=low+1):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low<=high:
        p_index=partition(arr,low,high)
        quick_sort(arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)
    return arr

nums=[4,1,7,6,3,2,8]
print(quick_sort(nums,0,len(nums)-1))

