# Initial implementation of linkedlist and traversal of this.

# Node class
class Node:
    # Function to initialize node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains a node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list, will start from head.
    def PrintList(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' ')
            tmp = tmp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second # Link the first node with second
second.next = third # link the second node with third

llist.PrintList()
