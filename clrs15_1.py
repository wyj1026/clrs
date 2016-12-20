# from bottom to top
def cut_rod(p,n):
    r = [0]
    for i in range(1,n+1):
        curr = 0
        for j in range(1,i+1):
            if j>len(p)-1:
                break
            curr = max(curr,p[j]+r[i-j])
        r.append(curr)
    return r[-1]
p = [0,1,5,8,9,10,17,17,20,24,30]
print(cut_rod(p,100))



#from top to bottom
def cut_rod2(p,n):
    r = {0:0}
    def find_result(p,n):
        if n in r:
            return r[n]
        else:
            curr=0
            for i in range(1,n+1):
                if i>len(p)-1:
                    break
                curr = max(curr,p[i]+find_result(p,n-i))
        r[n] = curr
        return r[n]
    return find_result(p,n)
print(cut_rod2(p,100))
