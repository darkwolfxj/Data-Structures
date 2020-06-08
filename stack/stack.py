import sys
sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#     def check(self):
#         if len(self.storage) != 0:
#             for i in self.storage:
#                 print(i)
#         else:
#             print("The stack is empty.")
#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) != 0:
#             return self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        count = 0
        current = self.storage.head
        tail = self.storage.tail
        done = False
        while done is False:
            if count == 0 and current == None:
                return count
            elif count == 0 and current.get_value() == tail.get_value():
                count = 1
                done = True
            elif current.get_value() != tail.get_value():
                current = current.get_next()
                count += 1
            else:
                count += 1
                done = True
        print(count)
        return count
    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.head != None and self.storage.tail != None:
            return self.storage.remove_tail()
        elif self.storage.head == None and self.storage.tail == None:
            return None
   
    def __repr__(self):
        count = 0
        current = self.storage.head
        tail = self.storage.tail
        done = False
        values = []
        while done is False:
            if count == 0 and current.get_value() == tail.get_value():
                count = 1
                values.append(current.get_value())
                done = True
            elif current.get_value() != tail.get_value():
                values.append(current.get_value())
                count += 1
            else:
                count += 1
                done = True
        return str(values)