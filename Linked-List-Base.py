class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node_end(self, node):

        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return       
        last = self.head
        while last.next:
            last = last.next        
        last.next = new_node
    
    def print_list(self):
        temp = self.head
        while temp:
            print("{} --> ".format(temp.data), end='')
            temp = temp.next

l = LinkedList()
l.insert_node_end(5)
l.insert_node_end(6)
l.insert_node_end(2)
l.insert_node_end(9)
l.insert_node_end(3)
l.print_list()