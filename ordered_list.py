class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None
        self.tail = None
    # self -> bool
    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head is None:
            return True
    # int -> bool
    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            new_node = Node(item)
            current = self.head
            while (current.next is not None) and (item > current.item):
                current = current.next  
            if (current.next is None) and (item > current.item):  # when the given number is the greatest among the numbers in a list
                current.next = new_node
                current.next.prev = current
                self.tail = new_node
            elif current.prev is None and current.item > item:  # when the given number is the smallest among the numbers in a list
                current.prev = new_node
                current.prev.next = current
                self.head = new_node
            elif item == current.item:
                return False
            else:  # when the given number is in between the smallest number and the greatest number
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
        return True
    # int -> bool
    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        new_node = Node(item)
        current = self.head
        if self.is_empty():   # if the list is empty
            return False
        elif current.item == item:
            if (current.next is None) and (current.prev is None):  # when there's only one element in the list
                self.head = None
                self.tail = None
                return True
        while current.item != item:
            if current.next is None:  # if the given item is not in the list
                return False
            current = current.next
        if current.next is None:  # when the first occurance of the given item is the last element
            current.prev.next = None
            self.tail = current.prev
        elif current.prev is None:  # when the first occurance of the given item is the first element
            current.next.prev = None
            self.head = current.next
        else:  # when the first occurance of the given item is in between the first element and the last element
            current.prev.next = current.next
            current.next.prev = current.prev
        return True
    # int -> int
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        current = self.head
        current_index = 0
        while current.item != item:
            if current.next is None:  # if the given item is not in the list
                return None
            current_index += 1
            current = current.next  
        return current_index
    # int -> int
    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        current = self.head
        current_index = 0
        if index == 0:
            if (current.next is None) and (current.prev is None):  # when there's only one element in the list
                self.head = None
                self.tail = None
                return current.item
        while current.next is not None: 
            if current_index == index: # when the current index matches the given index
                if index == 0:  # when the index is the first element
                    current.next.prev = None
                    self.head = current.next
                    return current.item
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return current.item
            current = current.next
            current_index += 1
        if current_index == index:  # when the index given matches with the index of the last element
            current.prev.next = None
            self.tail = current.prev
            return current.item
        raise IndexError
    # Node, int -> bool
    def search_helper(self, node, item):
        if self.is_empty():
            return False
        elif node.next is None:
            if node.item == item:  # when the given node is the last element
                return True
            return False
        elif node.item == item:
            return True
        node = node.next
        return self.search_helper(node, item)

    # int -> bool
    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        head = self.head
        return self.search_helper(head, item)

    # self -> list 
    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        current = self.head
        blk_list = []
        while current is not None:
            blk_list.append(current.item)
            current = current.next
        return blk_list

    # Node, list -> list
    def list_reversed_helper(self, node, lst):
        '''helper function for list_reserved. It prevents the unnecessary change of tail'''
        if node is None:
            return lst
        lst.append(node.item)
        node = node.prev
        return self.list_reversed_helper(node, lst)

    # self -> list
    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        blk_list = []
        tail = self.tail
        return self.list_reversed_helper(tail, blk_list)

    # Node, int -> int
    def size_helper(self, node, counter):
        if node is None:
            return counter
        node = node.next
        counter += 1
        return self.size_helper(node, counter)

    # self -> int
    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance''' 
        initial_count = 0
        head = self.head
        return self.size_helper(head, initial_count)
