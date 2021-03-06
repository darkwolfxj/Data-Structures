"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.results = []
    def __repr__(self):
        return f"{self.value}"
    # Insert the given value into the tree
    def insert(self, value):
        # if node is intantiated with None
        if self.value is None:
            # set self.value to inserted value
            self.value = value

        # else if node has a value and the inserted value is greater than or equal to that value
        elif value >= self.value:
            # check if node has a right
            if self.right:
                # do recursive function until reaching an empty right node
                self.right.insert(value)
            else:
                # insert new node with value
                self.right = BSTNode(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)                
            else:
                self.left = BSTNode(value)
   
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # recursively check if self.value == target
        # if base value is target, return true
        if self.value == target:
            return True
        if self.value > target:
            if self.left is not None:
                # recursively check down left 
                return self.left.contains(target)
        elif self.value < target:
            if self.right is not None:
                # recursively check down right 
                return self.right.contains(target)
        else:
            return False        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
                
        
        
       
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursively apply a function to both left and right as well as the base value
        if not self.left and not self.right:
            return fn(self.value)
        elif self.left and not self.right:
            return fn(self.value), self.left.for_each(fn)
        elif self.right and not self.left:
            return fn(self.value), self.right.for_each(fn)
        elif self.left and self.right:
            return fn(self.value), self.left.for_each(fn), self.right.for_each(fn)

# Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop(-1)
            print(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass            