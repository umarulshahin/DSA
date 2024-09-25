
#* Queue using two stack 

class stack:
    
    def __init__(self):
        self.s1=[]
        self.s2=[]
        
    def push(self,val):
        
        self.s1.append(val)
        
    def pop(self):
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.pop())