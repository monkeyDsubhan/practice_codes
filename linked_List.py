class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None #1st element of
    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

    #match to add a node at any index
    # indexing starts from 0
    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        position=0
        if position==index:
            self.insertAtBegin(data)
        else:

    def insertAtEnd(self,data):
        new_node =Node(data):
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while(current_node)


        