def sort_by_counting(A):
    C = []
    for x in range(max(A)+1):
        C.append(0)
    for x in range(len(A)):
        C[A[x]]+=1
    for x in range(max(A)):
        C[x+1] = C[x]+C[x+1]    
    B = A[:]
    '''
    stable:for the same numbers,their orders do not change
    '''
    for x in range(len(A)):
        k = len(A)-i-1
        B[C[A[k]]-1]=A[k]
        C[A[k]]-=1
    return B
text_case = [2,5,6,8,1,2,3,2,3,0,2,3,0,3]

