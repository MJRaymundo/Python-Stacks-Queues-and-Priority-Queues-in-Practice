# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# queues.py
# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python

from collections import deque
#Refactoring the Code Using a Mixin Class
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

#Building a Stack Queue Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#Building a Priority Queue Data type
from collections import deque
from heapq import heappop, heappush
from itertools import count

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]