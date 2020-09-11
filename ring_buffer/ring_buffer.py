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
            self.head.prev = self.tail
            self.head.next = self.tail
            self.tail.prev = self.head
            self.tail.next = self.head 
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
        #increase length of list
        self.length += 1
        
    def remove_from_head(self):
        #check if list is empty
        if self.length == 0:
            return None
        #check if one element in list
        elif self.length == 1:
            #save value that's being removed
            removed = self.head.value 
            #set the head and tail to none 
            self.head = None 
            self.tail = None 
            self.length -= 1 
            #return removed value 
            return removed 
        else:
            old_head = self.head
            self.head = old_head.next
            self.head.prev = self.tail 
            self.length -= 1
            return old_head.value 
        
    def add_to_head(self, value):
        new_node = ListNode(value)
        #saves old head as a variable
        old_head = self.head 
        #new node becomes the head
        self.head = new_node
        #set the head's next pointer to be the old head
        self.head.next = old_head
        #have the new head prev point to the tail
        self.head.prev = self.tail
        #set old head prev as self.head
        old_head.prev = self.head 
        #set tail's next pointer to be the new head
        self.tail.next = self.head 
        self.length += 1
        
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dlist = None 

    def append(self, item):
        #check if dlist is empty 
        if not self.dlist:
            #create dlist initizlied with the item
            node = ListNode(item)
            self.dlist = DoublyLinkedList(node)
            self.size += 1
        else:
            #check if at capacity
            if self.size == self.capacity:
                #remove head 
                self.dlist.remove_from_head()
                self.size -= 1
                #add the item to the head of the list
                self.dlist.add_to_head(item)
                self.size += 1
            else:
                #add the item to the tail of the list
                self.dlist.add_to_tail(item)
                self.size += 1

    def get(self):
        #checks if dlist is empty or none
        if not self.dlist or self.dlist.length == 0:
            return []
        elif self.dlist.length == 1:
            #create an empty list 
            items = []
            #add the head of the list's value to the array
            items.append(self.dlist.head.value )
            return items 
        else:
            #create an empty list 
            items = []
            #add the head of the list's value to the array
            items.append(self.dlist.head.value )
            #set up current node
            current_node = self.dlist.head.next
            #loop through the dlist until the current_node is the head again 
            while current_node != self.dlist.head:
                items.append(current_node.value)
                current_node = current_node.next
            # return the list
            return items 