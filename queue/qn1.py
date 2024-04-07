# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders.  

from collections import deque
import time
import threading
class Queue:
    def __init__(self):
        self.buffer=deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer)==0
    
food_order_queue=Queue()

def place_order(orders):
    for order in orders:
        print("Placing order",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def sev_order():
    time.sleep(1)
    while True:
        order=food_order_queue.dequeue()
        print("Now serving",order)
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1=threading.Thread(target=place_order,args=(orders,))
t2=threading.Thread(target=sev_order)
t1.start()
t2.start()
t1.join()
t2.join()