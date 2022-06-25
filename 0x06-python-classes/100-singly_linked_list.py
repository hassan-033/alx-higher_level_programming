#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        elif (type(next_node) != Node and next_node is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(data) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) != Node and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        NewNode = Node(value)
        if (self.__head is None):
            self.__head = NewNode
            return self.__head
        temp = self.__head
        if temp.data >= value:
            self.__head = NewNode
            self.__head.next_node = temp
            return self.__head
        while (temp.next_node):
            num = temp.next_node.data
            if num >= value:
                temp2 = temp.next_node
                temp.next_node = NewNode
                NewNode.next_node = temp2
                return self.__head
            temp = temp.next_node
        temp.next_node = NewNode
        return self.__head

    def __str__(self):
        temp2 = self.__head
        while temp2 is not None:
            if temp2.next_node is None:
                print(temp2.data, end="")
            else:
                print(temp2.data)
            temp2 = temp2.next_node
        return ""
