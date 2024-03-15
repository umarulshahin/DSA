class Node:
    
    def __init__(self,data):
        self.data =data
        self.ref =None
        
class L_list:
    
    def __init__(self):
        
        self.head = None 
        
    def print(self):
        
       if not self.head :
           
           print("linked List is empty..")
       else:
           
           next=self.head
           while next:
               
               print(next.data,"-->",end=" ")
               next = next.ref
               
    def add_begin(self,data):
        
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def delete_begin(self):
        
        if not self.head: 
            
            print("Link list is empty you can't delete data")
        else:
            
            self.head = self.head.ref
            
L=L_list()
L.add_begin(10)
L.add_begin(50)
L.add_begin(100)
L.add_begin(20)
L.delete_begin()

L.delete_begin()
L.print()
           