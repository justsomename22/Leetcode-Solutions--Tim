"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode object.
        :param val: The value of the node (default is 0).
        :type val: int
        :param left: The left child node (default is None, indicating no left child).
        :type left: TreeNode or None
        :param right: The right child node (default is None, indicating no right child).
        :type right: TreeNode or None
        """
        self.val = val   # Assigns the given value to the node.
        self.left = left  # Sets the left child of the node.
        self.right = right # Sets the right child of the node.

class Solution(object):
    """
    Solution class containing the method to find the maximum depth of a binary tree.
    """
    def maxDepth(self, root):
        """
        Calculates the maximum depth of a binary tree.
        The maximum depth is the length of the longest path from the root to a leaf node.
        :param root: The root node of the binary tree.
        :type root: TreeNode or None
        :rtype: int
        :return: The maximum depth of the binary tree. Returns 0 if the tree is empty (root is None).
        """
        # Base case: if the root of the tree (or subtree) is None, it means we've reached beyond a leaf node
        # or the tree is empty. In this case, the depth from here is 0.
        if not root:
            return 0

        # Recursive Depth First Search (DFS) function to explore the tree and calculate depth.
        def dfs(node):
            """
            Performs Depth First Search starting from a given node to calculate the depth of the subtree rooted at that node.
            :param node: The current node being visited in the DFS traversal.
            :type node: TreeNode or None
            :rtype: int
            :return: The maximum depth of the subtree rooted at the current node.
            """
            # Base case for DFS: if the current node is None, it means we've gone beyond a leaf.
            # The depth from a null node is 0.
            if not node:
                return 0

            # Recursively calculate the depth of the left subtree.
            left_depth = dfs(node.left)
            # Recursively calculate the depth of the right subtree.
            right_depth = dfs(node.right)

            # The depth of the subtree rooted at the current node is 1 (for the current node itself)
            # plus the maximum depth of either its left or right subtree.
            # We take the maximum because we are interested in the *longest* path to a leaf.
            return max(left_depth, right_depth) + 1

        # Initiate the DFS traversal from the root of the binary tree.
        # The result of this call will be the maximum depth of the entire tree.
        return dfs(root)


if __name__ == '__main__':
    """
    Main block to demonstrate the usage of the Solution class and test the maxDepth method.
    This block will only execute when the script is run directly (not imported as a module).
    """
    sol = Solution() # Create an instance of the 'Solution' class to use its methods.

    # Create a sample binary tree structure as described in the problem example: [3,9,20,null,null,15,7]
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    root = TreeNode(3)         # Create the root node with value 3.
    root.left = TreeNode(9)    # Create the left child of root with value 9.
    root.right = TreeNode(20)   # Create the right child of root with value 20.
    root.right.left = TreeNode(15) # Create the left child of node 20 with value 15.
    root.right.right = TreeNode(7)  # Create the right child of node 20 with value 7.
    
    # Create a sample binary tree structure as described in the problem example: [1,null,2]
    #      1
    #       \
    #        2
    root2 = TreeNode(1)         # Create the root2 node with value 1.
    root2.right = TreeNode(2)    # Create the right child of root2 with value 2.

    returned_result = sol.maxDepth(root)
    print(returned_result)
    returned_result2 = sol.maxDepth(root2)
    print(returned_result2)