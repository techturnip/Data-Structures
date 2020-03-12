"""Implement a doubly linked list data structure"""

class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return "empty"

        curr_node = self.head

        output = ''
        output += f'( {curr_node.value} ) <-> '

        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'( {curr_node.value} ) <-> '

        return output

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""

        # instantiate new node
        new_head = ListNode(value)

        # grab prev head
        old_head = self.head

        # increment length
        self.length += 1

        # if list is empty
        if self.head is None and self.tail is None:
            # set head to new_head
            self.head = new_head
            # set tail to new_head
            self.tail = new_head
        else:
            # new_node's next node is the old head
            new_head.next = old_head
            # old_head's prev node is the new_head
            old_head.prev = new_head
            # set head to new_head
            self.head = new_head

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""

        # if list is empty
        if self.head is None and self.tail is None:
            return

        # grab the head's value
        value = self.head.value

        # handle 1 node in list
        if self.head == self.tail:
            # set head and tail to None, back to 0 nodes
            self.head = None
            self.tail = None
            self.length -= 1
        # there are multiple ListNodes
        else:
            # next_head will be current head's next node
            next_head = self.head.next
            # set next_head.prev to None
            # erasing the ref to node to be removed
            next_head.prev = None
            # erase current head's next node
            self.head.next = None
            # set next head as the new head
            self.head = next_head
            # decrement length
            self.length -= 1

        return value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""

        # instantiate new node
        new_tail = ListNode(value)

        # grab prev tail
        old_tail = self.tail

        # increment length
        self.length -= 1

        # if list is empty
        if self.head is None and self.tail is None:
            # set head to new_head
            self.tail = new_tail
            # set tail to new_head
            self.head = new_tail
        else:
            # new_tail's prev node is the old tail
            new_tail.prev = old_tail
            # old_head's prev node is the new_head
            old_tail.next = new_tail
            # set tail to new_tail
            self.tail = new_tail

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""

        # if list is empty
        if self.head is None and self.tail is None:
            return

        # grab the tail's value
        value = self.tail.value

        # handle 1 node in list
        if self.head == self.tail:
            # set head and tail to None, back to 0 nodes
            self.head = None
            self.tail = None
            self.length -= 1
        # there are multiple ListNodes
        else:
            # next_tail will be current tail's prev node
            next_tail = self.tail.prev
            # set next_tail.next to None
            # erasing the ref to node to be removed
            next_tail.next = None
            # erase current tail's prev node
            self.tail.prev = None
            # set next tail as the new tail
            self.tail = next_tail
            # decrement length
            self.length -= 1

        return value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        pass

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        pass

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        pass

    def get_max(self):
        """Returns the highest value currently in the list"""
        pass


new_dll = DoublyLinkedList()
print(new_dll)
new_dll.add_to_head(5)
new_dll.add_to_head(3)
new_dll.add_to_tail(1)
print(new_dll)
removed_val = new_dll.remove_from_head()
print(new_dll)
print(removed_val)
removed_tail = new_dll.remove_from_tail()
print(new_dll)
print(removed_tail)
