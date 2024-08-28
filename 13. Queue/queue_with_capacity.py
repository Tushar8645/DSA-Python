"""
Queue with fixed capacity (Circular Queue)

Queue Operations
- Create Queue
- Enqueue
- Dequeue
- Peek
- isEmpty
- isFull
- Delete
"""


class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(item) for item in self.items]
        return " ".join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "The queue is full."
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1

                if self.start == -1:
                    self.start = 0

            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            first_element = self.start
            start = self.start

            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1

            self.items[start] = None
            return first_element

    def peek(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1


if __name__ == "__main__":
    custom_queue = Queue(5)
    print("isFull:", custom_queue.isFull())
    print("isEmpty:", custom_queue.isEmpty())
    custom_queue.enqueue(10)
    custom_queue.enqueue(20)
    custom_queue.enqueue(30)
    print(custom_queue)
    custom_queue.dequeue()
    print(custom_queue)
    print("Peek:", custom_queue.peek())
    custom_queue.delete()
    print(custom_queue)
