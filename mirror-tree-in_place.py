#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def mirror(root):
    if root is None:
        return
    else:
        #swapping the pointer of root of left and right poniter
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)
