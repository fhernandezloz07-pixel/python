# python Unit 8 examples:
# What is a binary tree?
'''
a leaf node means it has no children.
Doesnt necessarily mean it is the last branch in the tree
there a re multiple subtrees within a tree 
Build logic in the code that is in the right order (checking greater than or less than)
    How do we know whats sorted, if we are looking at a certain node, if you go to the left of the tree, the left node HAS to be less than!!!
How does the ordering in a BST help with reach oeprations?
- It allows you to decide whether to go left or right based on the value you are searching for, reducing the number of nodes
The tree Node Class
- Each treeNode contains a value
'''

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None

# Creating a root node
root = TreeNode(13)

# Creating children nodes
root.left = TreeNode(6)
root.right = TreeNode(21)

# what does it mean when we add a new node in a tree?
'''
1. Start the root
2. compare the value to be inserted with the current node's value
3. if the value is less, move to the left child; if greater, move to the right child
4. Repeat steps 2-3 until the correct position is found
5. Insert the new node as a leaf
6. KEY TAKEAWAY: Binary trees do not have Duplicates!

Safest and easiest place to delete a node is al the way at the bottom, at the leaf nodes because the ones on top have children.
3 main cases to consider when deleting a node: 
- Node has no children (leaf node).
- Node has one child.
- Node has two children.

Case 1: Node with no children 
Case 2: Node with one child (doesn't matter if it's a left child or a right child, as long as parent is established correcly!)
Case 3: Node with Two Children (Sucessor vs. Predecessor)

'''