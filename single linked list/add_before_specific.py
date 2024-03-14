
class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.ref = None
        
class L_list:
    
    def __init__(self):
        
        self.head = None
        
    def traverse(self):
        
        if not self.head :
            
            print("L list is empty......!")
        else:
            n=self.head
            while n:
                
                print(n.data,"--->",end=" ")
                n=n.ref
                
    def add_begin(self,data):
        
         new_node = Node(data)
         new_node.ref = self.head
         self.head =new_node
   
    def add_befor(self,data,x):
        
        if not self.head :
            
            print(" L list is empty...")
            return
        
        elif self.head.data == x:
            new_node =Node(data)
            new_node.ref =self.head
            self.head  = new_node
        else:
            n=self.head
            while n.ref:
                
                if n.ref.data == x:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found")
            else:
                
                new_node=Node(data)
                new_node.ref = n.ref
                n.ref = new_node
            
                
        
l=L_list()
l.add_begin(10)
l.add_begin(20)
l.add_befor(1000,10)

l.traverse()
