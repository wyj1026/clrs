def quicksort(A,p,r):
    if p<r:
        q = parition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def parition(A,p,r):
    i = p-1
    for x in range(r-p+1):
        if A[p+x]<=A[r]:
            key = A[i+1]
            A[i+1] = A[p+x]
            A[p+x] = key
            i+=1
    return i
A=[2,8,6,5,2,3,2,5,0]
quicksort(A,0,8)
print(A)

