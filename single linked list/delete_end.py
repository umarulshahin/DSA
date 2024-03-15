       
class Node:
    
    def __init__(self,data):
        
        self.data= data
        self.ref = None
        
class L_list:
    
    def __init__(self):
        
        self.head = None
        
    def print(self):
        
      if self.head is None:
          print("linked list is None")
      else:
          
          n=self.head
          while n:
              print(n.data)
              n=n.ref
    def add_begin(self,data):
        
        new_node =Node(data)
        new_node.ref=self.head
        self.head =new_node
        
    def delete_end(self):
        
        if self.head is None:
            
            print("linked list is empty..")
            
        elif self.head.ref is None:
            self.head = None
            
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None 
l=L_list()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)

l.delete_end()

l.print()
