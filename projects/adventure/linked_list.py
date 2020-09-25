class Node:
    def __init__(self, value, next_node=None):
        # value the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get value of the node
    def get_value(self):
        return self.value

    # method to get the node's next_node
    def get_next(self):
        return self.next_node

    # method to update the node's next_node to the input node
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap value in a node
        new_node = Node(value)
        # check if linked list is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node
        else:
            # update the last node's 'next_node' to the new node
            self.tail.set_next(new_node)
            # update 'self.tail' to point to the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, linked list has more than one node
        else:
            # store last node's value in another variable so we can return it
            val = self.tail.get_value()
            # need to set 'self.tail' to second-to-last node
            # only way is by traversing the whole linked list from the beginning

            # starting from the head, we'll traverse down to the second to last node
            # init another reference to keep track of where we are in the linked list
            # as we're iterating
            current = self.head

            # keep iterating until the node after 'current' is the tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()

            # set 'self.tail' to 'current'
            self.tail = current
            # set new tail's next_node to none
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set 'selef.head' to the old head's 'next_node'
            self.head = self.head.get_next()
            # return the old head's value
            return val

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at
        # update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if current value we're looking at matches target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the taget node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max value
            if current.get_value() > max_value:
                # if so, update our max value variable
                max_value = curent.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value
