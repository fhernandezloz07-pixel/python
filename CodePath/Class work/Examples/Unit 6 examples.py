# # Write a function to find the middle node of a singly linked list
# # 

# def Node: 
#     def__init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def findMiddleNode(head):
#     # Edge case
#     if (head == None):
#         return None

#     # Naie approach
#     # tempHead = head
#     # count = 1

#     # Optimized Approach
#     slow = head
#     fast = head

# #how do we know we have reached the end
#     while(fast is not None and fast.next is not None):
#         fast = fast.next.next
#         slow = slow.next

#     return slow

# # review and Evaluate (runtime?)

# a = 