class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next # the next node in the list
        
class LinkedList:
    def __init__(self):
        self.head = None # points to the first node in the list
        self.tail = None # points to the last node in the list
        self.length = 0
    def add_to_tail(self, value):
        # check if there is a tail
        # if there is no tail (empty list)
        if not self.tail:
        # create a new node
            new_tail = Node(value, None)
        # Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail( general case):
        else:
        # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
        # Set current tail to the next node
            old_tail = self.tail
            old_tail.next = new_tail
        # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1
    
    def remove_head(self):
        # If not head (empty list)
        if not self.head:
            return None
        # return none

        # List with one element:
        elif self.head == self.tail:
        # Set self.head to current_head.nex (which is also none)
            current_head =self.head
            self.head = None
        # set self.tail to none
            self.tail = None
        # decrement length by one
            self.length -= 1
            # Return current_ head.value
            return current_head.value 

        # If head exists, (General case)
        else:
        # Set self.head to current_head.next
            current_head =self.head
            self.head = current_head.next
        # decrement length by one
            self.length -=1
        # Return current_ head.value
            return current_head.value 

    def remove_tail(self):
        if self.tail == None:
            return None
        # List of one element:
        elif self.head == self.tail:
            # Save the current_tail.value
            current_tail = self.tail.value
            # set self.tail to none
            self.tail = None
            # set self.head to none
            self.head = None
            return current_tail

        # Check if there is a tail
        else:
        # start at the head and iterate to the next_to_last node
        # stop when current_node.next == self.tail
        # save the current tail value
        # set self.tail to current_node
        # Set current_node.next to none 
            current_tail = self.tail.value
            current_node =self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            self.tail = current_node
            self.tail.next = None
            return current_tail

    def remove_at_index(self, index):
        # check lenth > index
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target= self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return target.value

        # itterate through the loop to find index
        prev_node = self.head 
        for i in range(index-1):
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length -=1 
        return target.value
        