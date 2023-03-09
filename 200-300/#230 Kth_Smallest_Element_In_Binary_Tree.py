class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        return ans[k-1]
