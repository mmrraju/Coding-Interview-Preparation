"""Given the head of a linked list and an integer val, remove all the nodes of
the linked list that has Node.val == val, and return the new head."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


def removeElement(head, val):
    dummy_head = Node(-1)
    dummy_head.next = head

    curr_node = dummy_head
    while curr_node.next != None:
        if curr_node.next.data == val:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next
    return dummy_head.next

ll = LinkedList()
ll2 = LinkedList()
for i in range(int(input("Enter the number of elements: "))):
    ll.push(int(input()))

ll2.head = removeElement(ll.head, 4)
ll2.printList()
