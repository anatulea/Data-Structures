"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the root value is smaler than the value we want to insert
        if value < self.value:
            # ckeck if the left branch has any nodes
            if self.left == None:
                # if it doesn't we asign the left node to the new node 
                self.left = BSTNode(value)
            else:
                # if the left side has a node we run recursion on insert()
                self.left.insert(value)
        # else if the value is bigger than the root value 
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if root value is equal to the target
        if target == self.value:
            return True #return true if it is
        # check if the target is smaller than the root value
        if target < self.value: 
            # check if the left branch is empty
            if self.left == None:
                return False # return false if the branch is empty
            # use recursion to find target on the left branch trees
            return self.left.contains(target)
        # check if target is larger than the target value
        else:
            if self.right == None: # check if the right branch is empty
                return False # return false if the branch is empty
             # use recursion to find target on the right branch trees
            return self.right.contains(target)    

    # Return the maximum value found in the tree
    def get_max(self):
        # check if the root has a right branch
        if self.right != None:
            return self.right.get_max()
        else:
            # else if there is no right branch return root value 
            return self.value
        # go right until can't go more right

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
print(bst.insert(8))
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
