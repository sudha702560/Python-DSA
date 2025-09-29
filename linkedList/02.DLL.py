class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
        
        new_node.next = self.head 
        self.head.prev = new_node
        self.head = new_node 

    def insert_end(self,data):
        new_node = Node(data)

        # IF the LinkedList is empty
        if not self.head:
            self.head = new_node 
        
        temp = self.head 

        while temp.next:
            temp = temp.next 
        
        temp.next = new_node 
        new_node.prev = temp 

    def DLL_size(self):
        temp = self.head 
        size = 0 
        while temp.next:
            temp = temp.next
            size+=1
        return size
    # assuming 0-based indexing 
    def insert_in_middle(self,data,position):
        self.size = self.DLL_size(self)

        if position < 0 and position > self.size:
            return "Invalid position"

        if position ==0:
            self.insert_at_beginning(self,data) 
            return 
        
        if position == self.size:
            self.insert_end(self,data)
            return 
    
        new_node = Node(data)
        temp = self.head 

        for _ in range(position):
            temp = temp.next
        
        new_node.next = temp 
        new_node.prev = temp.prev 
        temp.prev.next = new_node 
        temp.prev = new_node 




        




        





        




        




