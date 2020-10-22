        
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None for i in range(capacity)]
        self.oldest = 0
        
    def append(self, item):
        if self.size != self.capacity:
            self.storage.pop(0)
            self.storage.append(item)
            self.size += 1
        else:
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            self.oldest += 1
            if self.oldest >= self.capacity:
                self.oldest = 0

    def get(self):
        if not self.storage[self.capacity - 1]:
            return []
        elif None in self.storage:
            count = self.capacity - 1 
            items = []
            while self.storage[count]:
                items.append(self.storage[count])
                count -= 1
            return items 
        else:
            return self.storage
        