class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None 
    
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 

        temp = self.head 
        while temp.next:
            temp = temp.next
        
        temp.next = new_node 

    def insert_after_node(self, k, data):
        temp = self.head 
        while temp and temp.data != k:
            temp = temp.next 
        
        new_node = Node(data)
        new_node.next = temp.next 
        temp.next = new_node
    
    # def print_list(self):
    #     temp = self.head 

    #     while temp:
    #         print(temp.data, end= "->")
    #         temp = temp.next 
    
    def Delete_node(self,value):
        if not self.head:
            return 

        if self.head.data == value:
            self.head = self.head.next
            return 
        
        temp  = self.head 
        while temp.next and temp.next.data!= value:
            temp = temp.next 
        
        if temp.next:
            temp.next = temp.next.next 


# Traversal --  Going to each and every node of the Linked List
    def traversal(self):
        temp = self.head 

        while temp:
            print(temp.data, end="->")
            temp = temp.next 
        print("None")

    def search(self,value):
        temp = self.head 
        position = 0

        while temp:
            if temp.data == value:
                print("Found at position", position)
                return "Found"
            temp = temp.next 
            position+=1
        
        return "Not Found"




l1 = LinkedList()

l1.prepend(41)
l1.append(23)
l1.append(53)
l1.insert_after_node(23,26)
# l1.print_list()
l1.traversal()





