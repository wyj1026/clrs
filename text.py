n = 2 
i = 0
A11=[]
A12=[[1]]
A21=[[1,2]]
A22=[[1,2]]
B11=[[1,2]]
B12=[[1,2]]
B21=[[1,2]]
B22=[[1,2]]
#print(A11.append(A12))
def ab():
    A=[1,2]
    B=[2,1]
    mid(A,B)
    print(A)
def mid(X,Y):
    X[0]=X[0]+Y[0]
    return X
ab()
