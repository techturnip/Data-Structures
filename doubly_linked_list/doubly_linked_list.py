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
        curr_tail = self.tail

        # increment length
        self.length += 1

        # if list is empty
        if self.head is None and self.tail is None:
            # set head to new_head
            self.tail = new_tail
            # set tail to new_head
            self.head = new_tail
        else:
            # new_tail's prev node is the old tail
            new_tail.prev = curr_tail
            # curr_tail's next node is the new_tail
            curr_tail.next = new_tail
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
        # handle if list is empty
        if self.head is None and self.tail is None:
            return

        # handle if node is already at the front
        if node is self.head:
            return

        # grab the value from node
        value = node.value

        # delete references
        # decrements length
        self.delete(node)

        # reinsert at the head
        # this will increment length back up
        self.add_to_head(value)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        # handle if list is empty
        if self.head is None and self.tail is None:
            return

        # handle if node is already at end
        if node is self.tail:
            return

        # grab the value from node
        value = node.value

        # delete node's refs
        # decrements length
        self.delete(node)

        # reinsert at the tail
        # this will increment the length back up
        self.add_to_tail(value)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""

        # no values in list
        if self.head is None and self.tail is None:
            return

        # if node is the head
        if node == self.head:
            # this will remove from head
            # and decrement length
            self.remove_from_head()
            return

        # if node is the tail
        if node == self.tail:
            # this will remove from tail
            # and decrement length
            self.remove_from_tail()
            return

        node.delete()
        self.length -= 1
        return

    def get_max(self):
        """Returns the highest value currently in the list"""
        curr_max = self.head.value
        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next

            if curr_node.value > curr_max:
                curr_max = curr_node.value

        return curr_max

    # LECTURE:
    def find_middle(self):
        """
        Return the middle node of the doubly linked list,
        if there are two nodes, return the left one,
        no emptylist, length >= 1
        1 - 2 - 3 = 2
        1 - 2 - 3 - 4 : 2
        """

        head = self.head

        tail = self.tail

        while head != tail and head.next != tail:
            head = head.next
            tail = tail.prev

        return head.value

    def reverse_list(self):
        """
        Reverse List
        - no recursion
        - nor store the dll in diff data structures
        """
        # store curr_node for iteration
        ch = self.head
        ct = self.tail

        while ch != ct:
            cleft = ch
            cright = ct

            if cleft == cright:
                return self

            if cleft.prev is None and cright.next is None:
                # swap head and tail
                cleft.prev = self.tail.prev
                cleft.next = None
                cright.next = self.head.next
                cright.prev = None

                self.head = cright
                self.tail = cleft

                # update adjacent relationship
                cright.next.prev = self.head
                cleft.prev.next = self.tail
                print(self.head.value)
                print(self.tail.value)

            # move right through list
            ch = ch.next
            # move left through list
            ct = ct.prev

            return self


new_dll = DoublyLinkedList()
new_dll.add_to_tail(3)
new_dll.add_to_tail(4)
new_dll.add_to_tail(5)
new_dll.add_to_tail(6)
print(new_dll)
new_dll.reverse_list()
print(new_dll)
