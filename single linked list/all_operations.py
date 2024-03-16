
class Node:
    
    def __init__(self,data):
        
        self.data =data
        self.ref =None
        
class L_list:
    
    def __init__(self):
        
        self.head = None
        
    def traverse(self):
        
        if self.head is None:
            
            print("Linked List is empty")
        else:
             next =self.head
             
             while next is not None:
                 
                 print(next.data,"--->",end=" ")
                 next = next.ref
    def add_begin(self,data):
        
        new_node=Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        
        new_node = Node(data)

        if  self.head is None:
            
            self.head =new_node
            
        else:
            
            next = self.head
            while next.ref:
                
                next=next.ref
            next.ref =new_node
            
    def add_after(self,data,x):
        next = self.head
        while next:
            if next.data == x:
                break
            next=next.ref
        if next is None:
            print("Node not in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = next.ref
            next.ref = new_node
            
    def add_before(self,data,x):
        
        if self.head is None:
            print("Linked List is empty .......!")
            return
        
        if self.head.data == x:
                
                new_node =Node(data)
                new_node.ref=self.head
                self.head = new_node
        else:
            
            next = self.head
            
            while next.ref:
                
                if next.ref.data == x:
                    break
                next =next.ref
                
            if next.ref is None:
                print(" node is not found linked list")
                
            else:
                
                new_node=Node(data)
                new_node.ref = next.ref
                next.ref = new_node
                
    def delete_begin(self):
        
        if not self.head:
            print("Linked List is empty you can delete Node") 
        else:
            self.head=self.head.ref
            
    def delete_end(self):
        
        if not self.head:
            print("Linked List is empty you can delete Node") 
            
        elif self.head.ref is None:

            self.head = None
        else:
            next=self.head
            while next.ref.ref is not None:
                next=next.ref
            next.ref=None
            
    def delete_by_node(self,x):
        
        if self.head is None:
            print("Linked List is empty you can delete Node") 
            
            return
        elif self.head.data == x:
            
            self.head = self.head.ref
        else:
            
            next=self.head
            while next.ref:
                
                if next.ref.data == x:
                    break
                next = next.ref
                
            if next.ref is None:
                print("Node not find")
            else:
                next.ref=next.ref.ref
    def New_node(self,data):
        
        if self.head :
            print("linked List is Not empty")
            
        else:
            
            new_node=Node(data)
            self.head = new_node
                
        
            
            
Li=L_list()
Li.New_node(30)
Li.add_begin(10)
Li.add_begin(20)
Li.add_end(500)
Li.add_after(50,20)
Li.add_before(100,50)
Li.delete_begin()
Li.delete_by_node(50)
Li.delete_end()
Li.New_node(30)
Li.traverse()
                 