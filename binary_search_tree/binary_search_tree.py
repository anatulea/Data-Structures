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
# from stack.stack import Stack 

# from stack import Stack
# import sys
# sys.path.append('../stack/')

# import sys
# path = sys.path.append('..')
# from stack.stack import Stack
import sys  
sys.path.append('/Users/anatulea/Documents/lambda/computer science/Data-Structures/stack')
from stack import Stack

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
    # O(n)
    def for_each(self, fn):
        # we will have to look at both branches 
        # start at the root 
        fn(self.value)
        if self.left is not None:
            # go to left
            self.left.for_each(fn)
        # else:
        #     pass
        if self.right is not None:
            # go to right
            self.right.for_each(fn)


    def for_each_iterative(self, fn):
        # Depth first traversal iterative:
        # Start at the root
        cur_node = self
        # push it on to the stack
        stack = Stack()
        # stack = [] we can use an array instead of the stack class
        # stack.append(cur_node)
        stack.push(cur_node)

        # While stack is not empty:
        while len(stack) > 0:
            cur_node = stack.pop()
            #push right
            if cur_node.right is not None:
                stack.push(cur_node.right)
            # push left 
            if cur_node.left is not None:
                stack.push(cur_node.left)
            # do the thing with the current node
            fn(cur_node.value)
        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        cur_node = self
        # print(cur_node.value)
        bfs_result = []
        # print(bfs_result)
        queue = []
        queue.append(cur_node)
        while len(queue) > 0:

            cur_node = queue.pop(0)
            
            bfs_result.append(cur_node.value)
            
            if cur_node.left is not None:
                queue.append(cur_node.left)
           
            if cur_node.right is not None:
                queue.append(cur_node.right)
                # print(bfs_result)
        # print(bfs_result)
            print(cur_node.value)

    def bft_print_recursive(self, queue , bfs_result):
        if len(queue) == 0:
            return bfs_result
        cur_node = queue.pop(0)
        bfs_result.append(cur_node.value)

        if cur_node.left is not None:
            queue.append(cur_node.left)
    
        if cur_node.right is not None:
            queue.append(cur_node.right)
        
        return self.bft_print_recursive(queue, bfs_result)
    

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
# print(bst.insert(8))
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# the shape of the binary tree
#          1
#        /  \
#  none      8
#           /
#          5
#       /    \
#      3     7
#    /  \   /
#  2    4  6 

print("recursive dft")
bst.for_each(print)
print('----------')
print("iterative dft")
bst.for_each_iterative(print)

print('=+++++++++++++++')
bst.bft_print()
# [1, 8, 5, 3, 7, 2, 4, 6]
print(bst.bft_print_recursive([bst], []))
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
