import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Runtime complexity : O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
BST for going through names 
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 
    
    #insert the given value into the tree
    def insert(self, value):
        #check if value is >= current node 
        if value < self.value:
            #check if left node space is open
            if not self.left:
                self.left = BSTNode(value)
            else:
                #check the value of the left node to the value we want to insert
                self.left.insert(value)
        else:
            #check if right node space is open
            if not self.right:
                self.right = BSTNode(value)
            else:
                #check the value of the right node to the value we want to insert
                self.right.insert(value)

    #returns true if the tree contains the value
    def contains(self, target):
        while self.value != target:
            #check left side of node 
            if self.value > target:
                if self.left:
                    self = self.left
                else:
                    return False
            else:
                if self.right:
                    self = self.right
                else:
                    return False
        return True 

nameTree = BSTNode(names_1[0])
#runtime complexity: O(n)
for name in names_1:
    if not nameTree.contains(name):
        nameTree.insert(name)

for name in names_2:
    if nameTree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
