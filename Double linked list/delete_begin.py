class Node:
    
    def __init__(self,data):
        
        self.data=data
        self.nref=None
        self.pref=None
        
class D_l_list:
    
    def __init__(self):
        
        self.head= None
        
    def f_print(self):
        
        if self.head is None:
            print("linked list is None")
            
        else:
            
            n=self.head
            while n:
                print(n.data,"-->",end=" ")
                n=n.nref
                
    def r_print(self):
        print()
        if self.head is None:
            print("Linked list is None")
            
        else:
            n=self.head
            while n.nref:
                n=n.nref
                
            while n:
                print(n.data,"-->",end=" ")
                n=n.pref
                
                
    def add_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list not empty")
        
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def delete_begin(self):
        
        if self.head is None:
            print("LInked list is empty can't delete") 
        
        elif not self.head.nref:
            self.head =None
        else:
            
            self.head=self.head.nref
            self.head.pref=None
d=D_l_list()
d.add_empty(10)
d.add_begin(20)
d.add_begin(30)
d.delete_begin()
d.f_print()
d.r_print()