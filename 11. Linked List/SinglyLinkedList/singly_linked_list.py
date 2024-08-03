class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = str()

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                result += " -> "

            temp_node = temp_node.next

        return result

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    # def insert(self, index, value):
    #     if index < 0 or index >= self.length:
    #         return False

    #     # new_node = Node(value)

    #     if index == 0:
    #         return self.prepend(value)
    #     elif index == self.length - 1:
    #         return self.append(value)
    #     else:
    #         new_node = Node(value)
    #         current_node = self.head

    #         for _ in range(index-1):
    #             current_node = current_node.next

    #         new_node.next = current_node.next
    #         current_node.next = new_node

    #     self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head

            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

        if index == self.length:
            self.tail = new_node

        self.length += 1
        return True

    def traverse(self):
        current_node = self.head

        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def search(self, target):
        current_node = self.head
        index = 0

        while current_node:
            if current_node.value == target:
                return index

            current_node = current_node.next
            index += 1

        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 1:
            return self.head
        else:
            current_node = self.head

            for _ in range(index):
                current_node = current_node.next

        return current_node

    def set_value(self, index, value):
        temp_node = self.get(index)

        if temp_node:
            temp_node.value = value
            return True

        return False

    def pop_first(self):
        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current_node = self.head

            while current_node.next is not self.tail:
                current_node = current_node.next

            self.tail = current_node
            current_node.next = None

        self.length -= 1
        return popped_node.value

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
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

    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    new_linked_list = LinkedList()
    new_linked_list.append(10)
    new_linked_list.append(20)
    new_linked_list.append(30)
    new_linked_list.prepend(40)
    new_linked_list.insert(4, 100)
    print(new_linked_list)
    new_linked_list.traverse()
    print("Search:", new_linked_list.search(40))
    print("Get:", new_linked_list.get(4))
    new_linked_list.set_value(2, 200)
    print(new_linked_list)
    print("Pop first:", new_linked_list.pop_first())
    print(new_linked_list)
    print("Pop:", new_linked_list.pop())
    print(new_linked_list)
    print("Remove:", new_linked_list.remove(3))
