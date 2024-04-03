#Deleting middle element from the singly linked list
class Node:  
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,value):
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node

    def delete_middle(self):
         slow=self.head
         fast=self.head
         prev=None

         while fast and fast.next:
              prev=slow
              slow=slow.next
              fast=fast.next.next
         prev.next=prev.next.next     



    def display(self):
        temp=self.head
        while temp:
            print(temp.value,end="==>")
            temp=temp.next

ll=linkedList()
ll.insert_at_beg(5)
ll.insert_at_beg(3)
ll.insert_at_beg(8)
ll.insert_at_beg(6)
ll.insert_at_beg(1)
ll.delete_middle()
ll.display()


            

