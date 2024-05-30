class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.value != q.value:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
