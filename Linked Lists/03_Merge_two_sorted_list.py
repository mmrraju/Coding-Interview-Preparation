class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None

    # Method to print linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    # Function to add of Node at the end
    def push(self, new_data):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


# Function to merge two sorted linked list
def mergeList(head1, head2):
    # Create a temp node null
    temp = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeList(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeList(head1, head2.next)

    return temp


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()

for i in range(int(input("Enter the First list element number: "))):
    ll1.push(int(input()))
for j in range(int(input("Enter the Second list element number: "))):
    ll2.push(int(input()))


ll3.head = mergeList(ll1.head, ll2.head)

ll3.printList()
