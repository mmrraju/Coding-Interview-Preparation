class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def DeleteNode(self, key):
        tmp = self.head
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                tmp = None
                return
        while tmp is not None:
            if tmp.data == key:
                break
            previous_node = tmp
            tmp = tmp.next
        if tmp == None:
            return
        previous_node.next = tmp.next
        tmp = None

    def PrintList(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()


llist = LinkedList()
for _ in range(int(input("How many node do you want: "))):
    m = int(input())
    llist.Push(m)
print("The linked list is : ")
llist.PrintList()
m = int(input("Which node do you want to delete ?: "))
llist.DeleteNode(m)
print("After deleting the node your linked list is: ")
llist.PrintList()
