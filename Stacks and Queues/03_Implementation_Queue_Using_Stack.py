"""Implement a first in first out (FIFO) queue using only two stacks.
 The implemented queue should support all the functions of a normal
 queue (push, peek, pop, and empty)."""


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def printQueue(self):
        return self.s1

    def peek(self):
        if self.s2:
            return self.s2[-1]
        elif self.s1:
            return self.s1[0]
        return None

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def isEmpty(self):
        if self.s1 or self.s2:
            return False
        return True


obj = MyQueue()
for i in range(1, 11):
    obj.push(i)
print(obj.printQueue())
print("Pop(): ", obj.pop())

print("Peek value: ", obj.peek())
print("Is empty: ", obj.isEmpty())

