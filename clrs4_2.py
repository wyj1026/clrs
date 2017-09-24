def strassen(matrix_A,matrix_B,n):
    if len(matrix_A)==1:
        return [[matrix_A[0][0]*matrix_B[0][0]]]
    else:
        P=make_matrixs(matrix_A,matrix_B,n)
        matrix_C = calculate_p(P,n)
        return matrix_C
def make_matrixs(matrix_A,matrix_B,n):
    S,A11,A12,A21,A22,B11,B12,B21,B22 = [],[],[],[],[],[],[],[],[]
    for i in range(int(n/2)):
        A11.append(list(matrix_A[i]))
        A12.append(list(matrix_A[i]))
        A21.append(list(matrix_A[int(n/2)+i]))
        A22.append(list(matrix_A[int(n/2)+i]))
        B11.append(list(matrix_B[i]))
        B12.append(list(matrix_B[i]))
        B21.append(list(matrix_B[int(n/2)+i]))
        B22.append(list(matrix_B[int(n/2)+i]))
        for j in range(int(n/2)):
            A11[i].pop()
            A12[i].pop(0)
            A21[i].pop()
            A22[i].pop(0)
            B11[i].pop()
            B12[i].pop(0)
            B21[i].pop()
            B22[i].pop(0)
    S.extend([redu(B12,B22)])
    S.append(plus(A11,A12))
    S.append(plus(A21,A22))
    S.append(redu(B21,B11))
    S.append(plus(A11,A22))
    S.append(plus(B11,B22))
    S.append(redu(A12,A22))
    S.append(plus(B21,B22))
    S.append(redu(A11,A21))
    S.append(plus(B11,B12))
    P = []
    P.append(strassen(A11,S[0],n/2))
    P.append(strassen(S[1],B22,n/2))
    P.append(strassen(S[2],B11,n/2))
    P.append(strassen(A22,S[3],n/2))
    P.append(strassen(S[4],S[5],n/2))
    P.append(strassen(S[6],S[7],n/2))
    P.append(strassen(S[8],S[9],n/2))
    return P
def calculate_p(P,n):
    C = []
    C11 = plus(plus(redu(P[3],P[1]),P[5]),P[4])
    C12 = plus(P[0],P[1])
    C21 = plus(P[2],P[3])
    C22 = plus(redu(redu(P[0],P[2]),P[6]),P[4])
    return make_matrix(C11,C12,C21,C22,n)
def make_matrix(a,b,c,d,n):
    matrix = []
    for i in range(int(n/2)):
        a[i].extend(b[i])
        matrix.append(a[i])
    for i in range(int(n/2)):
        c[i].extend(d[i])
        matrix.append(c[i])
    return matrix
        
def plus(A,B):
    n = len(A)
    if n == 1:
        return [[A[0][0]+B[0][0]]]
    else:
        C = []
        for i in range(n):
            C.append([])
            for j in range(n):
               C[i].append([])
        for i in range(n):
            for j in range(n):
                C[i][j] = A[i][j]+B[i][j]
        return C
def redu(A,B):
    n = len(A)
    if n == 1:
        return [[A[0][0]-B[0][0]]]
    else:
        C = []
        for i in range(n):
            C.append([])
            for j in range(n):
               C[i].append([])
        for i in range(n):
            for j in range(n):
                C[i][j] = (-B[i][j])
        return plus(A,C)
A = [[0,1,12,1,9,8,1,1],[2,3,1,1,7,6,1,1],[6,6,6,6,5,4,1,1],[5,5,4,3,3,2,1,1],[1,0,0,1,2,3,1,1],[9,9,9,9,9,9,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
B = [[3,2,1,0,4,5,1,1],[1,0,0,0,6,7,1,1],[1,23,2,1,8,9,1,1],[1,4,3,9,9,8,1,1],[7,6,5,4,3,2,1,1],[9,9,9,9,9,9,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
D = [[100,101],[102,103]]
E = [[10,11],[12,13]]
#print(make_matrix(A,B,D,E,6))
print(strassen(A,B,8))
#print(strassen([[-6,-5],[-3,-2]],[[4,2],[1,0]],2))
