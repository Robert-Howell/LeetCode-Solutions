class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        from collections import deque

        q = deque([root])
        levels = []

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(level)

        return levels[-1][0]
