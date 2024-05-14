class Node:
    def __init__(self, data, reference = None):
        self.data = data
        self.reference = reference

node1 = Node(5)
node2 = Node(11)
node1.reference = node2
print(node1.data)
print(node1.reference)

class LinkedList:
    def __init__ (self, head = None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print ('The linked list is empty')
        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data, c_node.reference)
                c_node = c_node.reference

    def add_to_start(self,data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

    def add_item(self,data):
        n_node = Node(data)
        if self.head is None:
            self.head = n_node
        else:
            c_node = self.head
            while c_node.reference is not None:
                c_node = c_node.reference
            c_node.reference = n_node

    def add_item_after(self, new_data, existing_data):
        if self.head is None:
            raise ValueError("The linked list is empty")
        
        n_node = Node(new_data)
        c_node = self.head
        while c_node is not None:
            if c_node.data == existing_data:
                n_node.reference = c_node.reference
                c_node.reference = n_node
                return
            c_node = c_node.reference
        raise ValueError(f"Node containing {existing_data} not found in the list")
    
    def remove_item(self, data):
        if self.head is None:
            raise ValueError("The linked list is empty")
        
        if self.head.data == data:
            self.head = self.head.reference
            return
        
        c_node = self.head
        while c_node.reference is not None:
            if c_node.reference.data == data:
                c_node.reference = c_node.reference.reference
                return
            c_node = c_node.reference
        raise ValueError(f"Node containing {data} not found in the list")


linked_list1 = LinkedList()
linked_list1.add_to_start(55)
# linked_list1.print_linked_list()
linked_list1.add_to_start(66)
# linked_list1.print_linked_list()
linked_list1.add_item(77)
linked_list1.print_linked_list()
linked_list1.add_item_after(100,66)
linked_list1.print_linked_list()
linked_list1.remove_item(77)
linked_list1.print_linked_list()