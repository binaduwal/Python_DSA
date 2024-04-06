# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". 
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def is_balanced(expression):
    stack=Stack()
    opening_brackets="({["
    closing_brackets=")}]"
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top=stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False
        
    return stack.is_empty()
        
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))   
print(is_balanced("((a+b))"))     
print(is_balanced("))"))          
print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) 

