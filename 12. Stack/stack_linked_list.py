"""
Create Stack using Linked List

Stack Operations
- Pop
- Push
- Peek
- isEmpty
- Delete
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        temp_node = self.head

        while temp_node:
            yield temp_node
            temp_node = temp_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        output = [str(data.value) for data in self.linked_list]
        return " -> ".join(output)

    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node
        self.linked_list.size += 1

    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            popped_node = self.linked_list.head
            self.linked_list.head = popped_node.next
            popped_node.next = None
            self.linked_list.size -= 1

            return popped_node

    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None
        self.linked_list.size = 0


if __name__ == "__main__":
    custom_stack = Stack()
    custom_stack.push(10)
    custom_stack.push(20)
    custom_stack.push(30)
    print(custom_stack)
    print("-" * custom_stack.linked_list.size * 5)
    custom_stack.pop()
    print(custom_stack)
    print("Peek:", custom_stack.peek())
    custom_stack.delete()
    print(custom_stack)
