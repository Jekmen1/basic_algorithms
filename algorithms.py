# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_start(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def insert_at_position(self, data, position):
#         if position < 0:
#             print("Invalid position")
#             return
#         if position == 0:
#             self.insert_at_start(data)
#             return
#         new_node = Node(data)
#         current = self.head
#         prev = None
#         count = 0
#         while current and count < position:
#             prev = current
#             current = current.next
#             count += 1
#         if count < position:
#             print("Position out of range")
#             return
#         new_node.next = current
#         prev.next = new_node
#
#     def delete_at_position(self, position):
#         if position < 0 or not self.head:
#             print("Invalid position or empty list")
#             return
#         if position == 0:
#             self.head = self.head.next
#             return
#         current = self.head
#         prev = None
#         count = 0
#         while current and count < position:
#             prev = current
#             current = current.next
#             count += 1
#         if not current:
#             print("Position out of range")
#             return
#         prev.next = current.next
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
#
# linked_list = LinkedList()
# linked_list.insert_at_start(1)
# linked_list.insert_at_end(3)
# linked_list.insert_at_end(4)
# linked_list.insert_at_end(5)
# linked_list.display()  # Output: 1 -> 3 -> 4 -> 5 -> None
#
# linked_list.insert_at_position(2, 1)  # Insert 2 at position 1
# linked_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
#
# linked_list.delete_at_position(2)  # Delete node at position 2
# linked_list.display()  # Output: 1 -> 2 -> 4 -> 5 -> None
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print("Stack is empty")
#             return None
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             print("Stack is empty")
#             return None
#
#     def is_empty(self):
#         return len(self.items) == 0
#
# # Test the implementation
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print("Stack:", stack.items)  # Output: [1, 2, 3]
#
# print("Peek:", stack.peek())  # Output: 3
# print("Stack after peek:", stack.items)  # Output: [1, 2, 3]
#
# print("Pop:", stack.pop())  # Output: 3
# print("Stack after pop:", stack.items)  # Output: [1, 2]
#
# print("Is stack empty?", stack.is_empty())  # Output: False
#
# print("Pop:", stack.pop())  # Output: 2
# print("Pop:", stack.pop())  # Output: 1
#
# print("Is stack empty?", stack.is_empty())  # Output: True
#
# print("Peek:", stack.peek())  # Output: Stack is empty; None
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)  # Output: [1, 2, 3]

print("Dequeue:", queue.dequeue())  # Output: 1
print("Queue after dequeue:", queue.items)  # Output: [2, 3]

print("Is queue empty?", queue.is_empty())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Is queue empty?", queue.is_empty())

print("Dequeue:", queue.dequeue())
