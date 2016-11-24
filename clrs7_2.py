def quick_sort(A,p,r):
    if p<r:
        q,k = partition(A,p,r)
        print(A,q,k)
        quick_sort(A,p,q-k)
        quick_sort(A,q+1,r)
def partition(A,p,r):
    i = 0
    key = A[r]
    number = 0
    j = r-1
    for x in range(r-p+1):
        if A[p+x]==key:
            number+=1
    for x in range(r-p+1):
        if A[p+x]==key:
            if p+x<j:
                change(A,p+x,j)
                j-=1
        if A[p+x]<=key:
            print(A,p+x,p+i)
            change(A,p+x,p+i)
            i+=1
    return p+i-1,number
def change(A,x,y):
    key=A[x]
    A[x]=A[y]
    A[y]=key
A = [3,2,4,5,3,1,123,21,0,9,13]
quick_sort(A,0,10)
print(A)
