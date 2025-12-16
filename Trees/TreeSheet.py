# TREE MASTERY ROADMAP - Complete Practice Sheet

# =============================================================================
# SECTION 1: ABSOLUTE BEGINNER FUNDAMENTALS
# =============================================================================

# 1. Create Binary Tree Node Class
# Topic: Node design
# Practice: Just write the class


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 


# 2. Manually Construct a Binary Tree
# Topic: Linking nodes

# 
"""
root = Node(1)
print(root.value)
root.left = Node(3)
root.right = Node(5)
root.left.left =Node(2)
"""


# 3. Preorder Traversal (Recursive)
# https://leetcode.com/problems/binary-tree-preorder-traversal/

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 

def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return 
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result 

root = Node(1)
print(root.value)
root.left = Node(3)
root.right = Node(5)
root.left.left =Node(2)
root.left.right =Node(6)
root.right.left =Node(22)
root.right.right =Node(30)

print(preorder(root))

"""


# 4. Inorder Traversal (Recursive)
# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 

def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.value)
        dfs(node.right)
    dfs(root)
    return result 

root = Node(1)
print(root.value)
root.left = Node(3)
root.right = Node(5)
root.left.left =Node(2)
root.left.right =Node(6)
root.right.left =Node(22)
root.right.right =Node(30)

print(inorder(root))
"""

# 5. Postorder Traversal (Recursive)
# https://leetcode.com/problems/binary-tree-postorder-traversal/

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 

def postoder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.value)
    dfs(root)
    return result 

root = Node(1)
print(root.value)
root.left = Node(3)
root.right = Node(5)
root.left.left =Node(2)
root.left.right =Node(6)
root.right.left =Node(22)
root.right.right =Node(30)

print(postoder(root))
"""

# 6. Level Order Traversal (BFS)
# https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 
from collections import deque
def level_order(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.extend(level)
    return result 
root = Node(1)
print(root.value)
root.left = Node(3)
root.right = Node(5)
root.left.left =Node(2)
root.left.right =Node(6)
root.right.left =Node(22)
root.right.right =Node(30)
print(level_order(root))

"""

#       1 
#    2     3 
#   4 5   6 7 


# result = [1,2,3,4, 5,6,7]
# q = [] 
# level = []




# root = Node(1)
# print(root.value)
# root.left = Node(3)
# root.right = Node(5)
# root.left.left =Node(2)
# root.left.right =Node(6)
# root.right.left =Node(22)
# root.right.right =Node(30)

# print(postoder(root))


# 7. Count Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/ (normal O(n) version first)
"""

def count_nodes(root):
    if not root:
        return 0 
    return 1 + count_nodes(root.left) + count_nodes(root.right)
"""

# root = Node(1)
# # print(root.value)
# root.left = Node(3)
# root.right = Node(5)
# # root.left.left =Node(2)
# root.left.right =Node(6)
# # root.right.left =Node(22)
# root.right.right =Node(30)

# print(count_nodes(root))
# 8. Height of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
def height(root):
    if not root:
        return 0 
    return 1 + max(height(root.left), height(root.right))
"""

# 9. Count Leaf / Full Nodes
# Practice on any tree
"""
def count_all_nodes(root):
    if not root:
        return 0
    if root.left and root.right:
        return 1 + count_all_nodes(root.left) + count_all_nodes(root.right)
    return count_all_nodes(root.left) + count_all_nodes(root.right)
"""

"""
def Count_leaves(root):
    if not root:
        return 0 
    if not root.left and not root.right:
        return 1 
    return Count_leaves(root.left) + Count_leaves(root.right)
"""
# 10. Sum of Leaf Nodes
# Practice on any tree

"""
def Count_leaves(root):
    if not root:
        return 0 
    if not root.left and not root.right:
        return root.value
    return Count_leaves(root.left) + Count_leaves(root.right)
"""


# 11. Print All Root to Leaf Paths
# https://leetcode.com/problems/binary-tree-paths/

"""
def path_to_leaf_nodes(root):
    if not root:
        return []
    result = []

    def dfs(node, path):
        path.append(str(node.value))
        if not node.left and not node.left:
            result.append("->".join(path))
        if node.left:
            dfs(node.left,path)
        if node.right:
            dfs(node.right, path)
        path.pop()
    dfs(root,[])

    return result 
root = Node(1)
# print(root.value)
root.left = Node(3)
root.right = Node(5)
# root.left.left =Node(2)
root.left.right =Node(6)
# root.right.left =Node(22)
root.right.right =Node(30)

print(path_to_leaf_nodes(root))
"""
# 12. Maximum Root to Leaf Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/ (simplified version)

"""
def max_path_sum(root):
    if not root:
        return 0 
    if not root.left and not root.right :
        return root.value
    
    left = max_path_sum(root.left) if root.left else float('-inf')
    right = max_path_sum(root.right) if root.right else float('-inf')
    
    return root.value + max(left , right)
"""

# =============================================================================
# SECTION 2: BEGINNER BST
# =============================================================================

# 13. Insert into BST
# https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
"""

# 14. Search in BST
# https://leetcode.com/problems/search-in-a-binary-search-tree/
"""
class Solution(object):
    def searchBST(self, root, val):
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root 
        return None

"""

# 15. Min & Max in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/ (use min/max logic)

# 16. Sorted Array to Balanced BST
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# 1 4 7 9 10 14 30

#       9 
#    4    14
#  1   7 10 30 
#             45

# 17. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/



# 18. Kth Smallest Element in BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# =============================================================================
# SECTION 3: LOWER INTERMEDIATE
# =============================================================================

# 19. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# 20. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# 21. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# 22. Same Tree
# https://leetcode.com/problems/same-tree/

# 23. Path Sum (I, II, III)
# https://leetcode.com/problems/path-sum/
# https://leetcode.com/problems/path-sum-ii/
# https://leetcode.com/problems/path-sum-iii/

# =============================================================================
# SECTION 4: HIGHER INTERMEDIATE
# =============================================================================

# 24. Lowest Common Ancestor (Binary Tree)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# 25. LCA in BST
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# 26. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# 27. Left Side View (reverse of above)

# 28. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# 29. Vertical Order Traversal
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# 30. All Nodes Distance K
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# 31. Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# =============================================================================
# SECTION 5: TREE CONSTRUCTION & SERIALIZATION
# =============================================================================

# 32. Construct BT from Preorder + Inorder
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# 33. Construct BT from Inorder + Postorder
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# 34. Serialize & Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# 35. Boundary Traversal
# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

# =============================================================================
# SECTION 6: ADVANCED TRANSFORMATIONS
# =============================================================================

# 36. Recover BST (two nodes swapped)
# https://leetcode.com/problems/recover-binary-search-tree/

# 37. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# 38. Populating Next Right Pointers II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# 39. Binary Tree Cameras
# https://leetcode.com/problems/binary-tree-cameras/

# 40. Count Complete Tree Nodes O(log² n)
# https://leetcode.com/problems/count-complete-tree-nodes/

# =============================================================================
# SECTION 7: N-ARY & TRIE
# =============================================================================

# 41. N-ary Tree Level Order
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# 42. Encode/Decode N-ary Tree
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

# 43. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

# 44. Word Search II (Trie + DFS)
# https://leetcode.com/problems/word-search-ii/

# =============================================================================
# SECTION 8: FENWICK & SEGMENT TREES
# =============================================================================

# 45. Binary Indexed Tree (Fenwick)
# https://practice.geeksforgeeks.org/problems/fenwick-tree/1

# 46. Segment Tree (Range Sum + Update)
# https://www.spoj.com/problems/FREQ2/ or build yourself

# 47. Segment Tree + Lazy Propagation
# https://www.spoj.com/problems/HORRIBLE/

# =============================================================================
# SECTION 9: COMPETITIVE PROGRAMMING HARD
# =============================================================================

# 48. Unique BSTs II (Generate All)
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# 49. Kth Ancestor - Binary Lifting
# https://www.spoj.com/problems/LCA/

# 50. Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/

# 51. Sum of Distances in Tree (Rerooting)
# https://leetcode.com/problems/sum-of-distances-in-tree/

# 52. Heavy-Light Decomposition (Intro)
# https://codeforces.com/problemset/problem/1172/E

# 53. Centroid Decomposition (Intro)
# https://codeforces.com/problemset/problem/321/C
