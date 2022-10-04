class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1. Singly Linked Lists

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)

linked_list = LinkedList()
linked_list.append(1) # 1, None
linked_list.append(2) # 1, 2 -> 2, None
linked_list.append(3) # 1, 2 -> 2, 3 -> 3, None
linked_list.append(4) # 1, 2 -> 2, 3 -> 3, 4 -> 4, None

node = linked_list.head
while node:
    print(node.value)
    node = node.next


# Exercise: Add a method to_list() to LinkedList that converts a linked list back into a Python list.
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        
        # TODO: Write function to turn Linked List into Python List
        
        lst = []
        node = self.head
        while node:
            #print(node.value)
            lst.append(node.value)
            node = node.next
        return lst

# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")


# 2. Doubly Linked Lists
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        
        # TODO: Implement this method to append to the tail of the list
        
        # Set value to head if head is None
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        
        # Move to the tail (the last node)        
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


# Test your class here

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous