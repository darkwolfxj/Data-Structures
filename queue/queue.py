import sys
sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
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

    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.head != None and self.storage.tail != None:
            return self.storage.remove_head()
        elif self.storage.head == None and self.storage.head == None:
            return None
