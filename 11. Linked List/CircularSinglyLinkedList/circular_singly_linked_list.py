class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print Circular Singly Linked List
    def __str__(self):
        temp_node = self.head
        result = str()

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:
                break

            result += ' -> '

        return result

    # Append method
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

    # Prepend Method
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.length += 1

    # Insert Method
    def insert(self, index, value):
        if index > self.length or index < 0:
            raise Exception('Index out of range')

        new_node = Node(value)

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node

        # if index == self.length:
        #     self.tail = new_node

        self.length += 1

    # Traversal
    def traversal(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

            if current == self.head:
                break

    # Search
    def search(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True

            current = current.next

            if current == self.head:
                break

        return False

    # Get method
    def get(self, index):
        if index >= self.length or index < 0:
            return None

        current = self.head

        for _ in range(index):
            current = current.next

        return current

    # Set method
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

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
            self.tail.next = self.head

        popped_node.next = None
        self.length -= 1

        return popped_node

    # Pop method
    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head

            while temp.next is not self.tail:
                temp = temp.next

            temp.next = self.head
            self.tail = temp
            popped_node.next = None

        self.length -= 1
        print(self.tail.value)
        return popped_node

    # Remove method
    def remove(self, index):
        print(self.length)
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None

        self.length -= 1

        return popped_node

    # Delete all nodes
    def delete_all(self):
        if self.length == 0:
            return

        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == '__main__':
    cs_linked_list = CSLinkedList()
    cs_linked_list.append(10)
    cs_linked_list.append(20)
    cs_linked_list.append(30)
    cs_linked_list.append(40)
    cs_linked_list.append(50)
    cs_linked_list.prepend(60)
    cs_linked_list.prepend(70)
    # cs_linked_list.insert(0, 60)
    print(cs_linked_list)
    # print('\nTraversal:')
    # cs_linked_list.traversal()
    # print('\nSearch:', cs_linked_list.search(50))
    # print('Get:', cs_linked_list.get(5))
    # print('Set value:', cs_linked_list.set_value(5, 309))
    # print(cs_linked_list)
    # print('Pop first:', cs_linked_list.pop_first())
    # print(cs_linked_list)
    # print('Pop:', cs_linked_list.pop())
    # print(cs_linked_list)
    print('Remove:', cs_linked_list.remove(6))
    print(cs_linked_list)
    print(cs_linked_list.length)
    # print(cs_linked_list.delete_all())
    # print(cs_linked_list)
