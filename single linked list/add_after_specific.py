
class Node:
    
    def __init__(self,data):
        
        self.data=data
        self.ref =None
    
class L_list:
    
    def __init__ (self):
        self.head = None
        
    def traverse(self):
        
        if not self.head:
            
            print("L_list is empty......!")
            
        else:
            
            n=self.head
            while n :
                
                print(n.data,"-->",end=" ")
                n=n.ref
                
    def add_bigin(self,data):
        
        new_node=Node(data)
        new_node.ref=self.head
        self.head = new_node
        
    def add_end(self,data):
        
        new_node = Node(data)
        
        if not self.head:
            
            self.head = new_node
            
        else:
            n=self.head
            while n.ref :
                n=n.ref
            n.ref = new_node
            
    def add_after(self,data,x):
        
        n=self.head
        
        while n:
            
            if n.data == x:
                break
            
            n=n.ref
            
        if not n:
            print("node not in linked List")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node    
        
        
            
l=L_list()
l.add_bigin(10)
l.add_bigin(20)
l.add_after(40,10)
l.add_after(50,20)
l.traverse()