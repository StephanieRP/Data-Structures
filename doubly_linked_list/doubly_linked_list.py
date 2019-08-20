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

    def add_to_head(self, value):
        added_node = ListNode(value)
        if self.head is None:
            self.head = added_node
        elif self.head is not None:
            current_head = self.head.value
            self.head = added_node
            self.head.insert_after(current_head)

    def remove_from_head(self):
        current_head = self.head
        self.head.delete()
        return current_head.value

    def add_to_tail(self, value):
        list_node = ListNode(value)
        if self.tail is None:
            self.tail = list_node
        else:
            prev_tail = self.tail
            self.tail = list_node
            self.tail.prev = prev_tail
            self.tail.insert_before(self.tail.value)

    def remove_from_tail(self):
        current_tail = self.tail
        self.tail.delete()
        return current_tail.value

    def move_to_front(self, node):
      # checks if only one item remains in the list
        if self.head is self.tail:
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def move_to_end(self, node):
      # checks if only one item remains in the list
        if self.head is self.tail:
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail  # set the current tail to be the node's prev
        node.next = None
        self.tail = node

    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.tail == node:
            self.remove_from_tail()
        elif self.head == node:
            self.remove_from_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    def get_max(self):

        current_max = None
        current_node = self.head

        while current_node is not None:
            if current_max is None or current_node.value > current_max:
                current_max = current_node.value

            current_node = current_node.next

        return current_max
