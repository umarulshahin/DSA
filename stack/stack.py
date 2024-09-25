
#* stack push and pop operations

stack=[]
def push():
    
    if len(stack) == n:
        print("stack is full")
    else:
        
        v=input("Enter values")
        stack.append(v)
        print(stack)
def pop():
    
    if not stack :
        print("stack is empty")
    else:
        print(stack.pop())
        print(stack)
n=int(input("enter the stack limit :"))
while True:
    
    print("select operation 1.push 2.pop 3.quit")
    op=int(input())
    if op ==1:
        push()
    elif op==2:
        pop()
    elif op ==3:
        break
    else:
        print("wrong options") 
        
    