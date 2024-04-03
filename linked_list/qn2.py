#Reverse linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node

    def reverse(self):
        prev=None
        current=self.head
        while current:
            nxt_node=current.next
            current.next=prev
            prev=current
            current=nxt_node
        self.head=prev
        

    def display(self):
        current=self.head
        while current:
            print(current.value,end="==>")
            current=current.next

ll=LinkedList()
ll.insert_at_end(2)            
ll.insert_at_end(9)            
ll.insert_at_end(4) 
ll.reverse()        
ll.display()   

    
