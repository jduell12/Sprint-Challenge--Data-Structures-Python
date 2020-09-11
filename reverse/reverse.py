class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    #runtime complexity: O(n)
    def reverse_list(self, node, prev): 
        #checks if list is empty:
        if not self.head:
            return None
        else:
            #prints out list before reversing it
            print('Before reverse')
            last_node = self.head
            while last_node:
                print(last_node.value)
                last_node = last_node.next_node
            print('---------------')
            
            #create pointer for previous node
            prev_node = None
            #create pointer for current node
            current_node = self.head
            #iterate over list 
            while current_node:
                #set next pointer as the current node's next
                next_node = current_node.next_node
                #set the current's next node as the previous
                current_node.next_node =  prev_node
                #swaps the prev node with current node 
                prev_node = current_node
                current_node = next_node
            #sets the head as the last prev node
            self.head = prev_node
            
            #prints out list after reversing it
            last_node = self.head
            print('After reverse')
            while last_node:
                print(last_node.value)
                last_node = last_node.next_node
            print('---------------')
            return self
        
        
    
