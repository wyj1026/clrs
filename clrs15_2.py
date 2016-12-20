def matrix_chain_order(p):
    cost = []
    for i in range(len(p)-1):
        cost.append([])
        for j in range(len(p)-1):
            cost[i].append(0)
    for l in range(2,len(p)):
        for i in range(0,len(p)-l):
            j=i+l-1
            cost[i][j]=1000000
            k=i
            while k<j:
                m = cost[i][k]+cost[k+1][j]+p[i]*p[k+1]*p[j+1]
                k+=1
                if m<cost[i][j]:
                    cost[i][j]=m
    return cost[0][len(p)-2]
print(matrix_chain_order([10,100,5,50]))

