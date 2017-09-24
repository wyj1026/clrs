def find_maximum_array(A,low,high):
    if low==high:
        return(A[low])
    else:
        mid = (low+high)//2
        left_sum = find_maximum_array(A,low,mid)
        right_sum = find_maximum_array(A,mid+1,high)
        cross_sum = find_maximum_cross_array(A,low,mid,high)
        return max(left_sum,right_sum,cross_sum)
def find_maximum_cross_array(A,low,mid,high):
    left_sum = -1000
    right_sum = -1000
    x = 0
    for i in range(mid-low+1):
        x = x+A[mid-i]
        if x>left_sum:
            left_sum = x
    x = 0
    for i in range(high-mid):
        x = x+A[mid+1+i]
        if x>right_sum:
            right_sum = x
    return (left_sum+right_sum)






def crack_array(A,low,high):
    max_A = A[high]
    for i in range(high-low+1):
        x = A[low+i]
        for j in range(high-low-i):
            x = x+A[low+i+j+1]
            if x>max_A:
                max_A = x
    return max_A

#for a in range(15):
print(crack_array([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],0,15))
print(find_maximum_array([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7],0,15))
