# Write a program to print binary numbers from 1 to 10 using Queue.  Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.

from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
        
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
def produce_binary_number(num):
    queue=Queue()
    queue.enqueue("1")

    for n in range(num):
        front=queue.front()
        print("  ",front)
        queue.enqueue(front+"0")
        queue.enqueue(front+"1")
        queue.dequeue()


produce_binary_number(10)
