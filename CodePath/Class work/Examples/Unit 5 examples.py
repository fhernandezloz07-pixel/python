class Node:
    def __init__(self, value): # Create an instance
        self.value = value
        self.next = None

a = Node(2)
b = Node(3)
c = Node(4)
d = Node(7)
e = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
print(a.value)
print(b.value)
print(c.next)

# how can we connect x to y?
