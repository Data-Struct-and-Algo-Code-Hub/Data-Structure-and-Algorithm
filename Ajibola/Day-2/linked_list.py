# using deque to create a linked list

# from collections import deque
# print(deque([1, 2, 3]))

# llist = deque(['a', 'b', 'c', 'd', 'e', 'f'])
# llist.appendleft('g')

# print(llist)

# Implementing a linked list

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node 
            return 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()

first_node = Node('a')
llist.head = first_node

second_node = Node('b')
print(second_node)
third_node = Node('c')

first_node.next = second_node
second_node.next = third_node
print(llist)

llist2 = LinkedList(['1', '2', '4', '5'])
print(llist2)

for data in llist2:
    print(data)

