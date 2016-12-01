from clrs6_4 import leaf_left,leaf_right,max_heapify,build_heap,is_full,make_full
 
def heap_maximum(array):
    return build_heap(array)[0]


def heap_extract_max(array):
    maximum = array[0]
    array[0]=0
    return maximum,max_heapify(array,1)

def heap_increase_key(array,x,key):
    array[x-1] = array[x-1]+key
    return build_heap(array)

def heap_insert(array,x):
    array.append(0)
    print(array)
    return heap_increase_key(array,len(array),x)

def parrent(array,x):
    if x//2 == 0:
        return int(x/2)
    else:
        return int((x-1)/2)
A=[1,2,3,4,5,6,7,8,9]
B=list(A)
C=list(A)
print(heap_maximum(A))
print(heap_extract_max(A))

print(heap_increase_key(build_heap(B),9,5.5))
print(heap_insert(build_heap(C),8.6))
