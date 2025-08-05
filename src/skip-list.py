"""
    - Understanding Python internals, Week 1-4
      building a small containers library.

      The goal is to understand the basic data 
      structures within, and also,
      to understand how the Data Model works
      within Python.

      CURRENT OBJECTIVE: 

      Create a functioning n-number Skip List,
      so this should have the same functionalit 
"""
class _Node:
    def __init__(self, level=0, data=None):
        self.level = level
        self.data = data
        self.forward = [None] * (level + 1)

    def __repr__(self):
        return f"{type(self).__name__}(data={self.data})"

"""
    - TO-DO:
      Implement insert, search, delete operations for the Skip List.
      Size change on demand.
"""
import math 

class SkipList:
    MAX_LEVEL = 16
    p = 0.5
    def __init__(self):
        self.head = _Node(MAX_LEVEL, None)
        self.current_level = 0
        self.size = 0
    
    def __len__(self):
        return self.size 

    
    def __contains__(self, item):
        node = self.head
        for level in range(self.current_level, -1, -1):
            while node.forward[level] and node.forward[level].data < item:
                node = node.forward[level]
        if node.forward[0] and node.forward[0].data == item:
            return True
        return False
    

    def __iter__(self):
        node = self.head.forward[0]
        while node is not None:
            yield node.data
            node = node.forward[0]

    def __repr__(self):
        return f"{type(self).__name__}(current_level={self.current_level}, size={self.size})"


    def add(self, item):
        pass
    

    def remove(self, item):
        pass


    def _generate_level(self, p):
        rand_levels = random.choice([x for x in range(0, 16)], p)
        return random.choice(rand_levels)

