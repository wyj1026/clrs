def search_by_divition(A,p,q,v):
    low = p
    high = q
    boo = False
    while low<=high:
        key = (low+high)//2
        mid = A[key]
        if mid<v:
            low = key+1
        elif mid>v:
            high = key-1
        elif mid==v:
            boo = True
            return((low+high)//2+1)
            break
    if not boo and low>high:
        return low
        

#insertion sort by search_by_divition
def insertion(li):
   i=1
   while i<len(li):     #the number of cycles is 1 less than len(A)
       key = li[i]
       j = i-1
       position=search_by_divition(li,0,j,key)
       for x in range(j-position+1):
           li[j+1-x]=li[j-x]
       li[position]=key
       i = i+1
   return li
print(insertion([98,456,45,4521,33,2,154,5,81]))

