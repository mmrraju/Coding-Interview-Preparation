# Linked List
A linked list is a data structure that represents a sequence of nodes. In a singly linked list, each node
points to the next node in the linked list. A doubly linked list gives each node pointers to both the next
node and the previous node.

Unlike an array, a linked list does not provide constant time access to a particular "index" within the list.
This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements.
The benefit of a linked list is that you can add and remove items from the beginning of the list in constant
time. For specific applications, this can be useful.

``` Runner Technique ```

The "runner" (or second pointer) technique is used in many linked list problems. The runner technique
means that you iterate through the linked list with two pointers simultaneously, with one ahead of the
other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each
one node that the "slow" node iterates through.
For example, suppose you had a linked list a 1 - >a 2 -> ••• ->an - >b 1 ->b 2 -> ••• ->bn and you wanted to
rearrange it into a 1 ->b 1 ->a 2 - >b 2 -> ••• - >an - >bn. You do not know the length of the linked list (but you
do know that the length is an even number).
You could have one pointer pl (the fast pointer) move every two elements for every one move that p2
makes. When pl hits the end of the linked list, p2 will be at the midpoint. Then, move pl back to the front
and begin "weaving" the elements. On each iteration, p2 selects an element and inserts it after pl

``` Recursive Technique ```
A number of linked list problems rely on recursion. If you're having trouble solving a linked list problem,
you should explore if a recursive approach will work. We won't go into depth on recursion here, since a later
chapter is devoted to it. However, you should remember that recursive algorithms take at least O ( n) space, where n is the depth
of the recursive call. All recursive algorithms can be implemented iteratively, although they may be much
more complex.

### Advantage of List

1. Dynamic Data Structure: Linked list is a dynamic data structure so it can grow and shrink at runtime by allocating and deallocating memeory. So there is no need to give initial size of linked list.

2. Insertion and Deletion: Insertion and deletion of nodes are really easier. Unlike array here we don’t have to shift elements after insertion or deletion of an element. In linked list we just have to update the address present in next pointer of a node.

3. Implementation: Data structures such as stack and queues can be easily implemented using linked list.

### Disadvantage of list

1. Memory Usage: More memory is required to store elements in linked list as compared to array. Because in linked list each node contains a pointer and it requires extra memory for itself.

2. Traversal: Elements or nodes traversal is difficult in linked list. We can not randomly access any element as we do in array by index. For example if we want to access a node at position n then we have to traverse all the nodes before it. So, time required to access a node is large.

3. Reverse Traversing: In linked list reverse traversing is really difficult. In case of doubly linked list its easier but extra memory is required for back pointer hence wastage of memory.
