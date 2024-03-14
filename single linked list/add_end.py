
class Node:
    
    def __init__(self,data):
        self.data = data 
        self.ref = None
        
class Link_list:
    
    def __init__(self):
        
        self.head = None
        
    def travers(self):
        
        if not self.head:
            print("empty....!")
            
        else:
            n=self.head
            while n:
                print(n.data,"-->",end=" ")
                n=n.ref
                
    def add_end(self,data):
        
        new_node = Node(data)
        
        if not self.head:
             
             self.head=new_node
        else:
            
            n=self.head
            while n.ref:
                 n = n.ref 
            n.ref = new_node        
    def add_bigin(self,data):
        
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
            
li = Link_list()
li.add_end(10)
li.add_end(100)
li.add_bigin(50)
li.travers()
