class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def isValidBST(self, root, f = float('-inf'), c = float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if root.val <= f or root.val>=c:
                return False

            return self.isValidBST(root.left,c=root.val) and self.isValidBST(root.right,f=root.val)


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(1)
    # t.right = TreeNode(1)
    t1 = Solution()
    v = t1.isValidBST(t)
    print(v)