"""
TREE DATA STRUCTURE THEORY

A tree is a nonlinear data structure used to represent hierarchical relationships. 
It consists of nodes connected by edges, where each node can contain zero or more children. 
A tree does not contain cycles and originates from a single starting point called the root.

Core Terminology

Root  
The topmost node in any tree structure. The traversal of a tree always begins from this node.

Parent Node  
A node that has at least one child.

Child Node  
A node that descends from a parent node.

Leaf Node  
Nodes that do not have any children. These appear at the last level of the tree.

Sibling Nodes  
Nodes that share the same parent.

Level  
The root exists at level zero. Each step downward increases the level count.

Height of a Tree  
Maximum number of edges between the root and any leaf.

Depth of a Node  
The number of edges from the root to the given node.

Types of Trees

General Tree  
A tree in which nodes can have any number of children.

Binary Tree  
A tree where every node has at most two children usually termed left child and right child.

Skew Tree  
A tree in which all nodes appear only on one side either left or right.

Full Binary Tree  
A binary tree in which every node has either zero or two children.

Complete Binary Tree  
All levels are completely filled except possibly the last. All nodes in the last level are placed left to right.

Binary Search Tree  
A special form of binary tree that maintains sorted order. 
Left subtree contains values smaller than the root. 
Right subtree contains values greater than the root.

Forest  
A collection of disjoint trees.

Operations on Trees

Insertion  
Adding a new node while preserving structural constraints. 
In a binary search tree values smaller go to left subtree others go to right.

Deletion  
Removing a node while maintaining the structure. 
Cases include node with no children node with one child and node with two children.

Searching  
Locating a value in the tree. 
Binary search tree allows logarithmic time search in balanced conditions.

Traversal  
Visiting all the nodes in a specific sequence.  
Depth first traversal includes inorder preorder postorder.  
Breadth first traversal visits every level from top to bottom.

Depth First Traversal Methods

Inorder  
Left child then root then right child.

Preorder  
Root then left child then right child.

Postorder  
Left child then right child then root.

Breadth First Traversal  
Also known as level order traversal. 
Visits one level at a time from left to right.

Binary Search Tree Properties

Left subtree stores smaller values.  
Right subtree stores larger values.  
Duplicate handling depends on implementation usually duplicates go to one side.

"""

# Working Code 

class Node:
    def __init__(self,value):
        self.value = value 
        self.left= None
        self.right = None 
    
class BinarySearchTree():
    def __init__(self):
        self.root = None 

    # insertion 
    def insertion(self, value):
        if self.root is None:
            self.root = Node(value)
            return 
        self._insertion(self.root,value)
    def _insertion(self , node , value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insertion(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insertion(node.right, value)


    def search(self, value):
        return self._search(self.root, value)


    def _search(self, node , value):
        if node is None:
            return False 
        if value == node.value:
            return True 
        
        if value < node.value:
            return self._search(node.left, value)
    
        if value > node.value:
            return self._search(node.right , value)
    

    # deletion 

    def delete(self,value):
        self.root  = self._delete(self.root,value)

    
    def _delete(self , node , value):
        if node is None:
            return node 
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        
        elif value > node.value:
            node.right = self._delete(node.right, value)
        
        else:
            # no children case 
            if node.left is None and node.right is None:
                return None 
            # There is one children case 
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left 
            
            # two children case 

            swapping_node = self._min_value(node.right)
            node.value = swapping_node
            node.right = self._delete(node.right, swapping_node)


        def _min_value(self , node):
            while node.left is not None:
                node = node.left 
            return node.value  

            

# Traversal 

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result 
    
    def _inorder(self,node,result):
        if node:
            self._inorder(node.left,result)
            result.append(node.value)
            self._inorder(node.right,result)
    
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result 
    
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._inorder(node.left,result)
            self._inorder(node.right,result)

    
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result 
    
    def _postorder(self, node, result):
        if node:
            self._inorder(node.left,result)
            self._inorder(node.right,result) 
            result.append(node.value) 

if __name__== "__main__":
    bst = BinarySearchTree()
    bst.insertion(40)
    bst.insertion(50)
    bst.insertion(66)
    bst.insertion(70)
    bst.insertion(30)

    print(bst.inorder())
    print(bst.postorder())
    print(bst.preorder())

    print(bst.search(170))
