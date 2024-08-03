"""
Create Stack with limit

Stack Operations
- Push
- Pop
- Peek 
- isFull
- isEmpty
- Delete
"""


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        if self.list == None:
            return "The stack is empty."
        else:
            values = reversed(self.list)
            output = [str(value) for value in values]
            return "\n".join(output)

    # isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # isFull method
    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    # Push method
    def push(self, value):
        if self.isFull():
            return "The stack is full."
        else:
            self.list.append(value)
            return "The element has been successfully inserted."

    # Pop method
    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list.pop()

    # Peek method
    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list[len(self.list) - 1]

    # Delete method
    def delete(self):
        self.list = None


if __name__ == "__main__":
    custom_stack = Stack(4)
    print(custom_stack.isEmpty())
    print(custom_stack.isFull())
    custom_stack.push(10)
    custom_stack.push(20)
    custom_stack.push(30)
    print(custom_stack)
    print("Pop:", custom_stack.pop())
    print(custom_stack)
    print("Peek:", custom_stack.peek())
    custom_stack.delete()
    print(custom_stack)
