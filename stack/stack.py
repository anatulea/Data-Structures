"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop()

"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""
# from singly_linked_list import LinkedList
# import sys
# sys.path.append('../singly_linked_list/')

import sys  
sys.path.append('/Users/anatulea/Documents/lambda/computer science/Data-Structures/singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
        return self.storage

    def pop(self):
        if self.size > 0:
            value = self.storage.remove_head()
            self.size -= 1
            return value
        else:
            return None

"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# LL use more memory than the arrays
# LL are faster at insertion and deletion
# LL are dynamic , arrays have fixed size
