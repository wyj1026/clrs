def binary_tree_insert(tree,leaf):
    while not tree==None:
        y=tree
        if tree.key<leaf.key:
            tree=tree.right
        else:
            tree=tree.left
        if leaf.key<y.key:
            y.left=leaf
        else:
            y.right=leaf


def binary_tree_delete(tree,node):
    if node.left==None:
        transplanet(tree,node,node.right)
    elif node.right==None:
        transplanet(tree,node,node.left)
    else:
# the key point is to find the successor of node.key
        y=node
        while not y==None:
            y = y.left
        y = y.p
        if not y.p==node:
            transplanet(tree,y,y.right)
            y.right=node.right
            y.right.p=y
        transplanet(tree,node,y)
        y.left=node.left
        node.left.p=y

