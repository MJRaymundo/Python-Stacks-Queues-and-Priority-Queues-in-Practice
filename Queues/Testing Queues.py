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

#print(fruits)
#['apple', 'orange', 'banana']

#Heapq 2
#from heapq import heappop

#heappop(fruits)
#'apple'

#print(fruits)
#['banana', 'orange']

#heapq priority
#person1 = ("John", "Brown", 42)
#person2 = ("John", "Doe", 42)
#person3 = ("John", "Doe", 24)

#print(person1 < person2)

#print(person2 < person3)

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


#print(messages.dequeue())

#(1, 'Radio station tuned in')

#Testing Prioirity Queue fix
#print(messages.dequeue())
#'Brake pedal depressed'

#print(messages.dequeue())
#'Hazard lights turned on'

#print(messages.dequeue())
#'Windshield wipers turned on'

#print(messages.dequeue())
#'Radio station tuned in'

#Not supported tuple comparisons
#from dataclasses import dataclass

#@dataclass
#class Message:
#    event: str


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