class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        temp_node = self.head

        while temp_node is not None:
            yield temp_node
            temp_node = temp_node.next


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(data) for data in self.linked_list]
        return " ".join(values)

    def enqueue(self, value):
        new_node = Node(value)

        if self.linked_list.head == None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

        self.linked_list.size += 1

    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            popped_node = self.linked_list.head

            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = popped_node.next

        self.linked_list.size -= 1
        return popped_node

    def peek(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None
        self.linked_list.size = 0


if __name__ == "__main__":
    custom_queue = Queue()
    custom_queue.enqueue(10)
    custom_queue.enqueue(20)
    custom_queue.enqueue(30)
    print(custom_queue)
    print(custom_queue.dequeue())
    print(custom_queue)
    print(custom_queue.peek())
