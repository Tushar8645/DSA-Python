# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


# Circular Doubly Linked List class
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = str()

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:
                break

            result += ' <-> '

        return result

    # def __iter__(self):
    #     temp_node = self.head

    #     while temp_node:
    #         yield temp_node
    #         temp_node = temp_node.next

    #         if temp_node == self.tail.next:
    #             break

    # Append method
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length += 1

    # Prepend method
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            self.head.prev.next = self.head
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head

        self.length += 1

    # Insert method
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of range")
            return

        new_node = Node(value)

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node

        self.length += 1

    # Traversal method
    def traverse(self):
        if self.length == 0:
            print("There is not any node for traversal")
        else:
            current_node = self.head

            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next

                if current_node == self.head:
                    break

    # Reverse traversal method
    def reverseTraverse(self):
        if self.length == 0:
            print("There is not any node for traversal")
        else:
            current_node = self.tail

            while current_node is not None:
                print(current_node.value)
                current_node = current_node.prev

                if current_node == self.tail:
                    break

    # Search method
    def search(self, target):
        if self.length == 0:
            return "There is not any node in Circular Doubly Linked List"
        else:
            current_node = self.head
            index = 0

            while current_node is not None:
                if current_node.value == target:
                    return index
                if current_node == self.tail:
                    return "The value does not exist in Circular Doubly Linked List"

                current_node = current_node.next
                index += 1

    # Pop first method
    def pop_first(self):
        if self.length == 0:
            return "There is not any node to delete"

        popped_node = self.head

        if self.length == 1:
            popped_node.next = None
            popped_node.prev = None
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = None

        self.length -= 1
        return popped_node

    # Pop method
    def pop(self):
        if self.length == 0:
            return "There is not any node to delete"

        popped_node = self.tail

        if self.length == 1:
            popped_node.next = None
            popped_node.prev = None
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.prev = None

        self.length -= 1
        return popped_node

    # Remove method
    def remove(self, index):
        if index < 0 or index > self.length:
            print("Index out of range")
            return

        if self.length == 0:
            return "There is not any node to delete"

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp_node = self.head

        for _ in range(index - 1):
            temp_node = temp_node.next

        popped_node = temp_node.next
        temp_node.next = popped_node.next
        popped_node.next.prev = temp_node
        popped_node.next = None
        popped_node.prev = None

        self.length -= 1
        return popped_node

    # Delete all nodes
    def delete_all(self):
        if self.length == 0:
            print('There is not any node in Circular Doubly Linked List')
        else:
            self.tail.next = None
            temp_node = self.head

            while temp_node is not None:
                temp_node.prev = None
                temp_node = temp_node.next

            self.head = None
            self.tail = None
            print('The Circular Doubly Linked List has beed successfully deleted')


if __name__ == "__main__":
    cd_linked_list = CircularDoublyLinkedList()
    cd_linked_list.append(10)
    cd_linked_list.append(20)
    cd_linked_list.append(30)
    cd_linked_list.prepend(40)
    cd_linked_list.prepend(50)
    cd_linked_list.insert(2, 100)
    print(cd_linked_list)
    # cd_linked_list.traverse()
    # cd_linked_list.reverseTraversal()
    cd_linked_list.reverseTraverse()
    print("Search:", cd_linked_list.search(10))
    print("Remove:", cd_linked_list.remove(-1))
    print(cd_linked_list)
    print(cd_linked_list.tail.value)
    cd_linked_list.delete_all()
    print(cd_linked_list)
