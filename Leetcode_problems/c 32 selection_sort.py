# Ascending Order

def selection_sort(lst):
    n=len(lst)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if lst[j]<lst[min_index]:
                lst[j],lst[min_index]=lst[min_index],lst[j]

    return lst

print(selection_sort([5,7,2,9,6]))




# Descending Order

def selection_sort(lst):
    n=len(lst)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if lst[j]>lst[min_index]:
                lst[j],lst[min_index]=lst[min_index],lst[j]

    return lst
        
print(selection_sort([5,7,2,9,6]))
