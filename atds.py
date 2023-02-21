"""
atds.py
"""

__author__ = "Adrian Lazzi"
__version__ = "2023-02-10"

class Stack(object): 
    def __init__(self):
        self.stack = []
    def push(self, item): 
        self.stack.append(item)
    def pop(self):
        return self.stack.pop(-1)
    def peek(self): 
        return self.stack[-1]
    def size(self): 
        return len(self.stack)
    def is_empty(self): 
        return (len(self.stack) == 0)
    def __repr__(self): 
        return super().__repr__() + str(self.stack)

class Queue(object):
    def __init__(self):
        self.queue = []
    def enqueue(self, item): 
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self): 
        return self.queue[0]
    def size(self): 
        return len(self.queue)
    def is_empty(self): 
        return (len(self.queue) == 0)
    def __repr__(self): 
        return super().__repr__() + str(self.queue)
    
class Deque(object): 
    def __init__(self):
        self.deque = []
    def add_front(self, item):
        self.deque.insert(0, item)
    def add_rear(self, item): 
        self.deque.append(item)
    def remove_front(self):
        return self.deque.pop(0)
    def remove_rear(self): 
        return self.deque.pop(-1)
    def size(self): 
        return len(self.deque)
    def is_empty(self):
        return (len(self.queue) == 0)
    def __repr__(self): 
        return "Deque" + str(self.deque)