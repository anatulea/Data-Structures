"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node 
        new_node = ListNode(value, None, None)
        # 1. add to empty
        if not self.head and not self.tail:
        # if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 2. add to nonempty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # update  list length
        self.length += 1
           
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value       
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        # if list is empty
        if not self.head and not self.tail:
            return
        # if list has one element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if the node to delete is the head
        if self.head == node:
            self.head = self.head.next
            node.delete() # uptades the prev and/or next
        # if the node to delete is the tail
        if self.tail == node:
            self.tail == self.tail.prev
            node.delete()
        # else if the node is anything else but head or tail
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0: 
            return None
        if self.length == 1:
            return self.head.value
    # create a max var     
        current = self.head
        max = self.head.value
    #  loop through nodes. we use while loops when we don't know how many
        while(current is not None):
            if current.value > max:
                max = current.value
            current = current.next
    # compare value in node to max found
    # return max found
        return max