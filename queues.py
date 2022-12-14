# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# queues.py
# Source: https://realpython.com/queue-in-python/#implementing-queues-in-python

from collections import deque

class Queue:
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

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#Building a Priority Queue Data type
from collections import deque
from heapq import heappop, heappush
from itertools import count

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]

# Testing FIFO queue

#from queues import Queue

#fifo = Queue()
#fifo.enqueue("1st")
#fifo.enqueue("2nd")
#fifo.enqueue("3rd")

#fifo.dequeue()

#fifo.dequeue()

#fifo.dequeue()

# Testing iterable FIFO Queue
#from queues import Queue
#fifo = Queue("1st", "2nd", "3rd")
#len(fifo)

#for element in fifo:
#    print(element)
#len(fifo)

#Testing Stack Data type
#from queues import Stack

#lifo = Stack("1st", "2nd", "3rd")
#for element in lifo:
#    print(element)

#Old python list
#lifo = []

#lifo.append("1st")
#lifo.append("2nd")
#lifo.append("3rd")

#lifo.pop()

#lifo.pop()

#lifo.pop()

#Heapq
#from heapq import heappush

#fruits = []
#heappush(fruits, "orange")
#heappush(fruits, "apple")
#heappush(fruits, "banana")

#fruits
#['apple', 'orange', 'banana']

#Heapq 2
#from heapq import heappop

#heappop(fruits)
#'apple'

#fruits
#['banana', 'orange']

#heapq priority
#person1 = ("John", "Brown", 42)
#person2 = ("John", "Doe", 42)
#person3 = ("John", "Doe", 24)

#person1 < person2
#True
#person2 < person3
#False

#Testing Priority Queue
#from queues import PriorityQueue

#CRITICAL = 3
#IMPORTANT = 2
#NEUTRAL = 1

#messages = PriorityQueue()
#messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
#messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
#messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
#messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

#messages.dequeue()
#(1, 'Radio station tuned in')

#Testing Prioirity Queue fix
#messages.dequeue()
#'Brake pedal depressed'

#messages.dequeue()
#'Hazard lights turned on'

#messages.dequeue()
#'Windshield wipers turned on'

#messages.dequeue()
#'Radio station tuned in'

#Not supported tuple comparisons
#from dataclasses import dataclass

#@dataclass
#class Message:
#     event: str


#wipers = Message("Windshield wipers turned on")
#hazard_lights = Message("Hazard lights turned on")

#wipers < hazard_lights
#Traceback (most recent call last):

#TypeError: '<' not supported between instances of 'Message' and 'Message'

#Fix is to enqueue with different priorities
#messages = PriorityQueue()
#messages.enqueue_with_priority(CRITICAL, wipers)
#messages.enqueue_with_priority(IMPORTANT, hazard_lights)

#Failing because of two messages being equal priority
#messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
#Traceback (most recent call last):

#TypeError: '<' not supported between instances of 'Message' and 'Message'