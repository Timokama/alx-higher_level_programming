#!/usr/bin/python3

class Node:
    """Class to represent node of singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of __data"""
        if type(value) is not int:
            raise TypeError ('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """getter of __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of __next_node"""
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """lass to store singly linked list of Node objects"""
    def __init__(self):
        """Initializes the linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position"""
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            head = self.__head
            if value < head.data:
                node.next_node = head
                self.__head = node
                return
            while head.next_node is not None:
                if value < head.next_node.data:
                    head.next_node = node
                    break
                head = head.next_node
            head.next_node = node

    def __str__(self):
        """String representation of SinglyLinkedList instance"""
        head = self.__head
        ret = ""
        if head is None:
            return ret
        while head.next_node is not None:
            ret += format(head.data, 'd')
            ret += '\n'
            head = head.next_node
        ret += format(head.data, 'd')
        return ret
