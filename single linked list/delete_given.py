
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
              print(n.data,"--->",end=" ")
              n=n.ref
    def add_begin(self,data):
        
        new_node =Node(data)
        new_node.ref=self.head
        self.head =new_node
        
    def delete_node(self,x):
        
        if not self.head :
           
           print("Linked List is empty")
           return 
       
        elif self.head.data == x:
            
            self.head = self.head.ref
        else:
            
            n=self.head
            while n.ref:
                
                if n.ref.data == x:
                    break
                n=n.ref
            if not n.ref : 
                print("node is not find")
            else:
                
                n.ref=n.ref.ref
                
l=L_list()
l.add_begin(10)
l.add_begin(20)
l.add_begin(30)
l.delete_node(20)
l.print()
