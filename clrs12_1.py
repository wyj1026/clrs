class binary_tree(object):
    def __init__(self,key):
        self.key=key
        self.right,self.left=None,None
def inorder_search_tree(tree):
    if not tree==None:
        inorder_search_tree(tree.left)
        print(tree.key)
        inorder_search_tree(tree.right)
def inorder_iteration_tree(tree):
    stack=[]
    res=[]
    while not tree==None or not len(stack)==0:
        while not tree==None:
            stack.append(tree)
            tree=tree.left
        while not len(stack)==0:
            top=stack.pop()
            res.append(top.key)
#if it is preorder,line 19 shoud be in 15
            tree=top.right
    return res
A=binary_tree(6)
A.left=binary_tree(5)
A.right=binary_tree(7)
A.left.left=binary_tree(2)
print(inorder_iteration_tree(A))
