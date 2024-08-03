class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # __str__ method
    def __str__(self):
        temp_node = self.head
        result = str()

        while temp_node:
            result += str(temp_node.value)

            if temp_node.next:
                result += ' <-> '

            temp_node = temp_node.next

        return result

    # Append method
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    # Perpend method
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # Traverse method
    def traverse(self):
        current_node = self.head

        while current_node:
            print(current_node.value)
            current_node = current_node.next

    # Reverse Traversal
    def reverseTraverse(self):
        current_node = self.tail

        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    # Search method
    def search(self, target):
        current_node = self.head
        index = 0

        while current_node:
            if current_node.value == target:
                return index

            current_node = current_node.next
            index += 1

        return -1

    # Get method
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            current_node = self.head

            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail

            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node

    # Set method
    def set(self, index, value):
        node = self.get(index)

        if node:
            node.value = value
            return True

        return False

    # Insert method
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print('Index out of bounds.')
            return

        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            new_node = Node(value)
            temp_node = self.get(index - 1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node

        self.length += 1

    # Pop first method
    def pop_first(self):
        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None

        self.length -= 1

    # Pop method
    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None

        self.length -= 1

    # Remove method
    def remove(self, index):
        if index > 0 or index == self.length:
            return None

        popped_node = self.get(index)

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None

        self.length -= 1

    # Delete all nodes
    def delete_all(self):
        if self.length == 0:
            print('There is not any node in Doubly Linked List')
        else:
            temp_node = self.head

            while temp_node is not None:
                temp_node.prev = None
                temp_node = temp_node.next

            self.head = None
            self.tail = None
            print('The Doubly Linked List has beed successfully deleted')


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(10)
    doubly_linked_list.append(20)
    doubly_linked_list.append(30)
    doubly_linked_list.prepend(40)
    doubly_linked_list.prepend(50)
    print(doubly_linked_list)
    print('\nTraversal')
    doubly_linked_list.traverse()
    print('\nReverse Traversal')
    doubly_linked_list.reverseTraverse()
    print('Search:', doubly_linked_list.search(10))
    print('Get:', doubly_linked_list.get(2))
    print('Set:', doubly_linked_list.set(2, 100))
    print(doubly_linked_list)
    doubly_linked_list.insert(5, 150)
    print(doubly_linked_list)
    doubly_linked_list.pop_first()
    print(doubly_linked_list)
    doubly_linked_list.pop()
    print(doubly_linked_list)
    print(doubly_linked_list.remove(0))
    print('Remove:', doubly_linked_list)
    doubly_linked_list.delete_all()
    print(doubly_linked_list)
