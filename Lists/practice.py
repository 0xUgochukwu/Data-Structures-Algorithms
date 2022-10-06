class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
# O(1)
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
    else:
        self.head, self.head.next = Node(value), self.head

# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend


# Test prepend - 0
linked_list = LinkedList()
linked_list.prepend(3)
linked_list.prepend(2)
linked_list.prepend(1)
assert linked_list.to_list() == [1, 2 ,3], f"list contents: {linked_list.to_list()}"


# O(n)
def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head is None:
        self.head = Node(value)
    else:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

LinkedList.append = append

# Test append - 0
linked_list = LinkedList()
linked_list.append(1) # 1, None
linked_list.append(2) # 1, 2 -> 2, None
linked_list.append(3) # 1, 2 -> 2, 3 -> 3, None
linked_list.append(4) # 1, 2 -> 2, 3 -> 3, 4 -> 4, None

assert linked_list.to_list() == [1, 2, 3, 4], f"list contents: {linked_list.to_list()}"