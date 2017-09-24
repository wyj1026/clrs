def merge_sort(A,p,r):
    if p<r:
        q = int((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A
def merge(A,p,q,r):
    L1 = []
    L2 = []
    for x in range(q-p+1):
        L1.append(A[p+x])
    for x in range(r-q):
        L2.append(A[q+1+x])
    for x in range(r-p+1):
        if L1==[]:
            for i in range(r-p+1-x):
                A[p+x+i] = L2[i]
            break
        elif L2==[]:
            for i  in range(r-p-x+1):
                A[p+x+i] = L1[i]
            break
        else:
            A[p+x]=(min(L1[0],L2[0]))
            if A[p+x]==L1[0]:
                L1.pop(0)
            else: 
                L2.pop(0)
    return A
print(merge_sort([6,3,2,1,32,1151,0,36],0,7))
