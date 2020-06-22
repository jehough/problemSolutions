class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.value == root2.value:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return False

def isSymmetric(root):
    return isMirror(root, root)

