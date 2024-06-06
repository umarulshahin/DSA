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
        
    def delete_after(self,x):
        
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n and n.data != x:
                n=n.ref
            if not n or n.ref is None:
                print("Node Note present")
            else:
                n.ref=n.ref.ref
            
L=L_list()
L.add_begin(10)
L.add_begin(50)
L.add_begin(100)
L.add_begin(20)
L.delete_after(40)
L.print()
           