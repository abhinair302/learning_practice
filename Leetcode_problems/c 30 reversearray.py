def rev(lst,left,right):
    if left>=right:
        print(lst)
        return 
    else:
        temp=lst[left]
        lst[left]=lst[right]
        lst[right]=temp
        rev(lst,left+1,right-1)

rev([5,7,3,2,6,1,5,9],2,5)
