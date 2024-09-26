class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def log(self):
        iterator = self.head
        output = ""
        while iterator:
            output += str(iterator.data)
            iterator = iterator.next
        print(output)

    def insert_at(self, value, position):
        if position == 0:
            self.head = Node(value, self.head)
        elif self.get_length() >= position > 0:
            iterator = self.head
            index = 0
            while iterator:
                if index == position - 1:
                    break
                iterator = iterator.next
                index += 1
            iterator.next = Node(value, iterator.next)
        else:
            print(f"Position {position} is invalid!")

    def get_length(self):
        iterator = self.head
        length = 0
        while iterator:
            iterator = iterator.next
            length += 1
        return length

    def delete(self, position):
        iterator = self.head
        index = 0
        if (self.get_length() > position > 0):
            while iterator:
                if index == position - 1:
                    iterator.next = iterator.next.next
                    break
                iterator = iterator.next
                index += 1
        elif position == 0:
            if iterator.next:
                self.head = iterator.next
            else:
                self.head = None


ll = LinkedList()
ll.insert_at(1, 0)
ll.insert_at(2, 1)
ll.insert_at(3, 2)
ll.delete(2)
ll.log()
