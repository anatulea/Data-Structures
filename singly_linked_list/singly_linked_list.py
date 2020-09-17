#todo a class that represents the individual elements in our ll
class Node:
    def __init__(self, value = None, next_node= None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return  self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None
        
    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        if self.head is None:
           # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:    
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
         # create a new node
        new_node = Node(value)
        # 1. Linked list empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        # 2. Linked List is Not empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            #update self.tail
            self.tail = new_node
            

    def remove_head(self):
        # Empty list
        if self.head is None:
            return None
        # Else, return Value of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 element
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
            return ret_value


    def remove_tail(self):
        # Empty list
        if self.head is None:
            return None
        else:
            pre = self.head
            temp = self.head.next_node
            while temp.next_node is not None:
                pre = pre.next_node
                pre.next_node = None
            del temp
            self.tail = pre

    def contains(self, value):
         # loop through linked list until next pointer is None
        current_node = self.head
        while current_node is not None:
            #if we find 'value'
            if current_node.get_value() == value:
                return True
        return False

    def get_max(self):
        pass
        # TODO time permitting