def insertion(li):
    i=1
    while i<len(li):     #the number of cycles is 1 less than len(A)
        key = li[i]
        j = i-1
        while j>=0 and li[j]>key: #for each i calculate the left []
            li[j+1] = li[j]
            j = j-1
        li[j+1]=key
        i = i+1
    print(li)
def insertion_large_to_small(li):
    i = 1
    while i<len(li):
        key = li[i]
        j = i-1
        while j>=0 and li[j]<key:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = key
        i = i+1
    print(li)
insertion([2342,4,45,2,45,1])
insertion_large_to_small([12,21,5,45,456,11,123,32])



#pratice
#2.1-3
def find_i(li,v):
    for x in range(len(li)-1):
        if li[x] == v:
            i = x
    
find_i([123,231,2123,45,4545,6],6)


#2.1-4
def sum_of_num(li_a,li_b):
    num_a = 0
    num_b = 0
    for x in range(len(li_a)):
         num_a = num_a+li_a[len(li_a)-1-x]*2^x
         print(num_a)
    for x in range(len(li_b)):
         num_b = num_b+li_a[len(li_b)-1-x]*2^x
    print(num_a,num_b)
sum_of_num([1,0,1],[1,1])





