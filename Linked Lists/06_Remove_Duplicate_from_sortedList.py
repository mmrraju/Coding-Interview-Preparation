class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert element at the endpoint
    def push(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def deleteList(self, key):
        temp = self.head
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted keep track of the previous.
        while temp is not None:
            if temp.data == key:
                break
            prev = temp.data
            temp = temp.next
        if temp is None:
            return
        # Unlink the node from linkedlist
        prev.next = temp.next
        temp = None

    def removeDuplicate(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head


ll = LinkedList()
for i in range(int(input("Enter the number of elements: "))):
    ll.push(int(input()))

ll.printList()
print('\n')
ll.removeDuplicate()
ll.printList()
