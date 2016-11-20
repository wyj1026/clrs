def leaf_left(array,i):
    if 2*i-1 >= len(array):
	    return 0
    else:
        return array[2*i-1]
def leaf_right(array,i):
    if 2*i >= len(array):
        return 0
    else:
        return array[2*i]
def max_heapify(array,i):
    left_leaf = leaf_left(array,i)
    right_leaf = leaf_right(array,i)
    if left_leaf == 0 and right_leaf == 0:
        return array
    elif left_leaf == 0 and not right_leaf == 0:
         if right_leaf>array[i-1]:
             key = array[i-1]
             array[i-1] = array[2*i]
             array[2*i] = key
             return array
         else:
             return array
    elif not left_leaf == 0 and right_leaf == 0:
         if left_leaf>array[i-1]:
             key = array[i-1]
             array[i-1] = array[2*i-1]
             array[2*i-1] = key
             return array
         else:
             return array
    else:
        max_ = max(array[i-1],left_leaf,right_leaf)
        if max_ == array[i-1]:
            return array
        elif max_ == left_leaf:
            key = array[i-1]
            array[i-1] = array[2*i-1]
            array[2*i-1] = key
            max_heapify(array,2*i)
            return array
        elif max_ == right_leaf:
            key = array[i-1]
            array[i-1] = array[2*i]
            array[2*i] = key
            max_heapify(array,2*i+1)
            return array
def build_heap(array):
    start_length = len(array)
    if not is_full(array):
        make_full(array)
    length = len(array)
    for i in range(length-int((length+1)/2)):
            max_heapify(array,length-int((length+1)/2)-i)
    return array[:start_length]
def is_full(array):
    boo = False
    for i in range(7):
        if 2**(i+1)==len(array)+1:
            boo = True
            break
    return boo
def make_full(array):
    if not is_full(array):
        array.append(0)
        make_full(array)
    return array
def heap_sort(array):
    result = list(array)
    heap_array = build_heap(array)
    for i in range(len(result)):
        result[i] = heap_array[0]
        heap_array[0] = 0
        max_heapify(heap_array,1)
    return result
print(heap_sort([1,5,6,7,8,9,65,45,12,232,1,2,22]))
