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

# O(n)
def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head
    while node.next:
        if node.value == value:
            return node
        node = node.next

LinkedList.search = search

# Test search
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)

assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here    
    if self.head is None:
        return

    # 1st element
    if self.head.value == value:
        self.head = self.head.next
        return
   
    # Other elements
    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next # remove(2) 1.next -> (2) -> 3
            return
        node = node.next

LinkedList.remove = remove

# Test remove - 0
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.remove(2)
assert linked_list.to_list() == [1, 3, 4], f"list contents: {linked_list.to_list()}"


def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head is None:
        return
    
    node = self.head
    self.head = self.head.next
    
    return node.value

LinkedList.pop = pop


# Test pop
value = linked_list.pop()
# assert value == 2, f"list contents: {linked_list.to_list()}"
# assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# O(1)
def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here
    if self.head is None:
        self.append(value)
        return
    
    if pos == 0:
        self.prepend(value)
        return
    
    idx = 0
    node = self.head
    while node.next and idx <= pos:
        if idx == pos - 1:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return
        node = node.next
        idx += 1
    else:
        self.append(value)

LinkedList.insert = insert

# Test insert - 0
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.insert(5, 2)
linked_list.to_list()


# O(1)
def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    count = 0
    node = self.head
    while node:
        count += 1
        node = node.next
    return count

LinkedList.size = size