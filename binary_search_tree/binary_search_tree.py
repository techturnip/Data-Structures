import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # insert left side
        if value < self.value:
            # there isn't a self.left for this node
            if not self.left:
                # insert into self.left
                self.left = BinarySearchTree(value)
            else:
                # there is a self.left, recurse to the left
                self.left.insert(value)
        # insert right side
        else:
            # there isn't a self.right for the current node
            if not self.right:
                # insert into self.right
                self.right = BinarySearchTree(value)
            else:
                # there is a self.right, recurse to the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # base case
        if target == self.value:
            return True

        # if target is smaller go left
        if target < self.value:

            # if nowhere else to go
            if not self.left:
                return False

            # recurse left side
            else:
                return self.left.contains(target)

        # if target is bigger go right
        elif target > self.value:

            # if nowhere else to go
            if not self.right:
                return False

            # recurse right side
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if left node
        if node.left:
            # recurse down the left side
            node.in_order_print(node.left)

        # print left side then root then right side
        print(node.value)

        # if right node
        if node.right:
            # recurse down the right side
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue
        queue = Queue()

        # add current node to queue
        queue.enqueue(node)

        while queue.len() > 0:
            # store next node to print
            curr_node = queue.storage.tail.value

            # dequeue node
            queue.dequeue()
            # print node
            print(curr_node.value)

            # add children to queue
            if curr_node.left:
                queue.enqueue(curr_node.left)
            if curr_node.right:
                queue.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a node stack
        stack = Stack()

        # push current node onto stack
        stack.push(node)

        while stack.len() > 0:
            # grab the current node
            curr_node = stack.storage.head.value

            # print the curr node value
            print(curr_node.value)
            # pop it off
            stack.pop()

            # if there is a right node
            if curr_node.right:
                # push node onto stack
                stack.push(curr_node.right)
            # if there is a left node
            if curr_node.left:
                # push node onto stack
                stack.push(curr_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
