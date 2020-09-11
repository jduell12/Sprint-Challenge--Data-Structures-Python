"""
List node for the doubly linked list incorporated in Ring buffer
"""
class ListNode:
    def __init__(self, value, next=None, prev=None):
        self.prev = prev
        self.next = next
        self.value = value 
"""
Doubly Linked list to be used in Ring Buffer 
"""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length 
    
    def add_to_tail(self, value):
        #creates new node 
        new_node = ListNode(value)
        
        #checks if empty list
        if self.length == 0:
            #set new node as head and tail
            self.head = new_node
            self.tail = new_node 
        #check if one element in list
        elif self.length == 1:
            #set new node as tail
            self.tail = new_node
            #set tail prev as current head which points to self.tail as next 
            self.tail.prev = self.head 
            self.head.next = self.tail 
            self.head.prev = self.tail 
            #set tail next as head
            self.tail.next = self.head 
        else:
            #save old tail 
            old_tail = self.tail
            #set new node as current tail
            self.tail = new_node
            #set old tail next to point to new tail
            old_tail.next = self.tail 
            #set current tail prev to point to the old tail
            self.tail.prev = old_tail 
            #set the tail's next to be the head
            self.tail.next = self.head 
            #set the head's prev as the new tail
            self.head.prev = self.tail
        
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dlist = None 

    def append(self, item):
        pass

    def get(self):
        pass