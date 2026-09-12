def pal(left,right,name):
    if left>=right:
        return True
    elif name[left]!=name[right]:
        return False
    else:
        return pal(left+1,right-1,name)

name="nitin"
print(pal(0,len(name)-1,name))