def radix_sort(A,d):
    for x in range(d):
        A = sort_on_x(A,x+1)
    return A
def sort_on_x(A,x):
    A_d = []
    for i in range(len(A)):
        A_d.append(int(A[i]/(10**(x-1)))%10)
    C = []
    for i in range(max(A_d)+1):
        C.append(0)
    for i in range(len(A_d)):
        C[A_d[i]]+=1
    for i in range(max(A_d)):
        C[i+1]+=C[i]
        C[i]-=1
    C[-1]-=1
    B = A_d[:]
    for i in range(len(A)):
        j = len(A)-i-1
        B[C[A_d[j]]]=A[j]
        C[A_d[j]]-=1
    return B[:]
textcase=[12,32,56,21,23,10,41]
radix_sort(textcase,2)
    
    
                                 
