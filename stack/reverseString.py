
#* String reverse using stack 

stack=[]

def push(val):
    
    stack.append(val)
    
    
def reverse(s):
    
    for i in s:
        push(i)
    re=""
    while stack:
        re+=stack.pop()
    print(re)
    
reverse("hello")