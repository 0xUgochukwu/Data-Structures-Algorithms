# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    curr, prev = linked_list.head, None
    # This loop will make the list point backwards so that node.next is actually node.prev
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    
    # return prev
    node = prev
    llist = LinkedList()
    while node:
        llist.append(node.value)
        node = node.next
        
    return llist

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)
    
flipped = reverse(llist)
print(flipped)