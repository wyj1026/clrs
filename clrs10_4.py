class binary_tree(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def search_all_keys(tree):
    if tree.right==None and tree.right==None:
        print(tree.key)
    else:
        print(tree.key)
        if tree.right==None:
            search_all_keys(tree.left)
        elif tree.left==None:
            search_all_keys(tree.right)
        else:
            search_all_keys(tree.left)
            search_all_keys(tree.right)
A=binary_tree(9)
A.left=binary_tree(8)
A.right=binary_tree(7)
search_all_keys(A)
