"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
   """
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop()

"""
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
"""
from singly_linked_list import LinkedList
import sys
sys.path.append('../singly_linked_list/')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size <= 0:
            # if len(self.storage) == 0:
            return None
        else:
            value = self.storage.remove_head()
            self.size -= 1
            return value


"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""
# linked lists(LL) consume more memory because they store the value and the pointer
# LL performes faster addition to the end and removal from the front than the Arrays
# Arrays use less memory but if the size is exceded they need to be copied(fixed size)
# LL have dynamic size
# Arrays delete and insert takes more time

"""
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# we need two stacks say stack1 and stack2 and we have maintain them such that the element entered first
# is always at the top of the stack stack1. This way, for dequeue, we just need to pop from stack1.
# But for enqueueing, we have to make the enqueued item reach the bottom of the stack.
# For that, we will have to pop the elements of stack1 one by one and push them onto stack 2, then add the new item to stack1 ,
# And then again pop everything from stack2 and push it back to stack 1., so the new item is now at the last.


class QueuesWithStacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        for i in range(len(self.stack1)):
            item = self.stack1.pop()
            self.stack2.append(item)
        self.stack1.append(data)
        for i in range(len(self.stack2)):
            item = self.stack2.pop()
            self.stack1.append(item)
        return

    def dequeue(self):
        if len(self.stack1) == 0:
            print('Queue empty')
            return
        else:
            return self.stack1.pop()

    def print_queue(self):
        if len(self.stack1) == 0:
            print("Queue Empty")
            return
        for i in range(len(self.stack1) - 1, 0, -1):
            print(f'{self.stack1[i]} <<-- ', end='')
        print(self.stack1[0])
        return


my_queue = QueuesWithStacks()
my_queue.enqueue(2)
my_queue.enqueue(5)
my_queue.enqueue(0)
my_queue.print_queue()

my_queue.dequeue()
my_queue.print_queue()
#5 <<-- 0

# 5
my_queue.enqueue(9)
my_queue.print_queue()
#5 <<-- 0 <<-- 9

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
