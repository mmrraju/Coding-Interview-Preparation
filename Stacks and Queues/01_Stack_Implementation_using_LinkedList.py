'''Stack implementation using a linked list'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # String representation of the stack
    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            out += str(curr.data) + " "
            curr = curr.next
        return out

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Check the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.data

    def pop(self):
        if self.isEmpty():
            raise Exception("Poping from an empty stack")
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.data

    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


stack = Stack()
for i in range(1, 11):
    stack.push(i)
print(f"Stack: {stack}")
stack.printStack()
stack.pop()
print('\n')
print(f"Stack: {stack}")
stack.printStack()
