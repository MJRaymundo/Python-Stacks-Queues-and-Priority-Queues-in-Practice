# queues.py

from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
# Testing FIFO queue

#from queues import Queue

#fifo = Queue()
#fifo.enqueue("1st")
#fifo.enqueue("2nd")
#fifo.enqueue("3rd")

#fifo.dequeue()

#fifo.dequeue()

#fifo.dequeue()