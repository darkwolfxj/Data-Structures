"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node 
            self.tail= new_node
            self.length += 1
        else:    
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is not None:    
            head_value = self.head.value
            self.delete(self.head)
            return head_value
        else:
            return
            
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.head == None and self.tail == None:
            new_node = ListNode(value)
            self.head = self.tail = new_node
            self.length += 1
        else:    
            new_node = ListNode(value, self.tail, None)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is not None:
            tail_value = self.tail.value
            self.delete(self.tail)
            return tail_value
        else:
            return
            
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        elif self.head.next is None:
            return
        elif node is self.tail:
                self.remove_from_tail()
                self.add_to_head(node.value)
        else:    
            node.delete()
            self.add_to_head(node.value)
            self.length -= 1
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.head:
            self.delete(self.head)
            self.add_to_tail(node.value)
        elif node is self.tail:
            print("Tail already at end.")
            return
        else:
            self.delete(node)
            self.length -= 1
            self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # deleted node is head or tail:
        if node is self.head or node is self.tail:
            # dll has 1 item
            if self.length < 2:
                self.head.delete()
                self.tail.delete()
                self.head = None
                self.tail = None
                self.length -= 1
            # dll has more than 1 item and node is head
            elif node is self.head:
                head = self.head
                self.head.delete()
                self.head = head.next
                head.next.prev = None
                self.length -= 1
            # dll has more than 1 item and node is tail
            elif node is self.tail:
                tail = self.tail
                self.tail.delete()
                tail.prev.next = None
                self.tail = tail.prev
                self.length -= 1
        # 1 item and node is not head or tail
        elif self.length > 2 and node is not self.head:
            print("Node does not exist in list.")
            return
        else:
            current = self.head
            while current != node:
                current = current.next
            if current != node:
                print("Node does not exist in list.")
                return 
            else:
                node.delete()
                self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        new_max = 0
        if current_node is self.head and self.head is self.tail:
            new_max = current_node.value
            return new_max
        else:
            while current_node != None:
                try:
                    if current_node.value > new_max:
                       new_max = current_node.value
                    else:
                        pass
                    current_node = current_node.next
                    if current_node is self.tail:
                        if current_node.value > new_max:
                            new_max = current_node.value
                            return new_max
                        else:    
                            return new_max
                except:
                    pass 
            
            

node = ListNode(1)
dll = DoublyLinkedList(node)
print(dll.get_max())