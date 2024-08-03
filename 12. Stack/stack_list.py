"""
Create Stack using List without size limit

Stack Operations
- Create Stack
- Push
- Pop
- Peek
- isEmpty
- isFull
- deleteStack
"""


class Stack:
    def __init__(self):
        self.list = list()

    def __str__(self):
        if self.list == None:
            return "There is not any element in the stack."
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

    # Push method
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted."

    # Pop method
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list.pop()

    # Peek method
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.list[len(self.list) - 1]

    # Delete method
    def delete(self):
        self.list = None


if __name__ == "__main__":
    custom_stack = Stack()
    custom_stack.push(10)
    custom_stack.push(20)
    custom_stack.push(30)
    print(custom_stack)
    print("isEmpty:", custom_stack.isEmpty())
    print("Pop:", custom_stack.pop())
    print("\nStack after pop element")
    print(custom_stack)
    print("\nPeek:", custom_stack.peek())
    custom_stack.delete()
    print(custom_stack)
