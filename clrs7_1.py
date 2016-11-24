def hoare_quick_sort(A,p,r):
    if p<r:
        q = hoare_partition(A,p,r)
        print(A,q)
        if q>p:
            hoare_quick_sort(A,p,q)
        if r>q+1:
            hoare_quick_sort(A,q+1,r)
def hoare_partition(A,p,r):
    key = A[p]
    i = p-1
    j = r+1
    while i<j:
        i+=1
        j-=1
        while A[i]<key:
            i+=1
        while A[j]>key:
            j-=1
        if i<j:
            x = A[i]
            A[i] = A[j]
            A[j] = x
            print(i,j,A)
        else:
            break
    return j
A=[10,9,8,7,6,5,4,3,2,1,0]
hoare_quick_sort(A,0,10)
print(A)
