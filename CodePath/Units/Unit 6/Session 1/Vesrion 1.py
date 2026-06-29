
# Problem 1:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node(4, Node(3, Node(2)))
print(head.value, "->", head.next.value, "->",  head.next.next.value)
# What did yiu learn? 
# the basic structure was head = Node(1, Node(2)) so we can use that
# and apply it to our problem so we can also return istead of 1 -> 2 we can do 4 -> 3 -> 2

# Problem 2:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
    
#head = Node(4, Node(3, Node(2)))
#print(head.value, "->", head.next.value, "->",  head.next.next.value)


def count_element(head, val):
    count = 0
    current = head 
    
    while current:
        if current.value == val:
            count += 1 
        current = current.next 
    return count

# # Input List: 3 -> 1 -> 2 -> 1

head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head, 1))
# What is space complexity?!?!