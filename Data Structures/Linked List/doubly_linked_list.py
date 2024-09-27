class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        if self.head:
            self.head.prev = Node(None, value, self.head)
            self.head = self.head.prev
        else:
            self.head = Node(None, value, self.head)

    def log(self, direction):
        itr = self.head
        output = ""
        if direction == 0:
            while itr:
                output += str(itr.data) + "->"
                itr = itr.next
            print(output)
        else:
            while itr.next:
                itr = itr.next
            while itr:
                output += str(itr.data) + "->"
                itr = itr.prev
            print(output)

    def linked_list_length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        print(length)
        return length

    def insert_at(self, position, value):
        if position == 0:
            self.head = Node(None, value, self.head)
        elif position > 0 and position < self.linked_list_length():
            index = 0
            itr = self.head
            while itr:
                if index == position - 1:
                    itr.next.prev = Node(itr, value, itr.next)
                    itr.next = Node(itr, value, itr.next)
                    break
                itr = itr.next
                index += 1
        else:
            return ValueError

    def delete_at(self, position):
        if position == 0:
            self.head = self.head.next
            self.head.prev = None
        elif position > 0 and position < self.linked_list_length():
            index = -1
            itr = self.head
            while itr:
                if index == position - 1:
                    itr.next.next.prev = itr
                    itr.next = itr.next.next
                    break
                itr = itr.next
                index += 1
        else:
            return IndexError


linked_list = LinkedList()
linked_list.insert_head(3)
linked_list.insert_head(2)
linked_list.insert_head(1)
linked_list.insert_at(3, 10)
linked_list.log(0)
linked_list.delete_at(0)
linked_list.log(0)
