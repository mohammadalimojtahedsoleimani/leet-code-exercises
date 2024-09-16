class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# main func 
def maxDepth(root):
    if root is None:
        return 0
    else:
        depth_left = maxDepth(root.left)
        depth_right = maxDepth(root.right)
        return max(depth_left,depth_right) + 1
