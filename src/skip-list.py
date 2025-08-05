"""
    - Understanding Python internals, Week 1-4
      building a small containers library.

      The goal is to understand the basic data 
      structures within, and also,
      to understand how the Data Model works
      within Python.
"""
class Node:
    def __init__(self, level, data):
        self.level = level
        self.data = data

    def __repr__(self):
        return f"Node<[{level}[{data}]>"


class SkipList:
    
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __init__    
