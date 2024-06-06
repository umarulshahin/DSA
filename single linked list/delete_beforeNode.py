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
        
    def delete_before(self,x):
        
        if self.head is None or self.head.data==x:
            print("Node can't delete")
        else:
            prev=None
            n=self.head
            while n.ref and n.ref.data!=x:
                prev=n
                n=n.ref
            if n.ref is None:
                print("node not present")
            elif not prev:
                self.head=n.ref
            else:
                prev.ref=n.ref
                         
            
L=L_list()
L.add_begin(10)
L.add_begin(50)
L.add_begin(100)
L.add_begin(20)
L.delete_before(10)
L.print()
           