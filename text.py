def find(A,x,y):
    X,Y=False,False
    for i in range(len(A)):
            if A[i]==x:
                X=i
            if A[len(A)-i-1]==y:
                Y = len(A)-i-1
            if type(X)==int and type(Y)==int:
                return [X,Y]
nums=[0,4,3,0]
nums_=nums[:]
nums_.sort()

