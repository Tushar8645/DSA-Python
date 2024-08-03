"""
Queue using Python List - no size limit

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
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.items == None:
            return "There is no element in the Queue"
        else:
            values = [str(item) for item in self.items]
            return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


if __name__ == "__main__":
    custom_queue = Queue()
    custom_queue.enqueue(10)
    custom_queue.enqueue(20)
    custom_queue.enqueue(30)
    print(custom_queue)
    custom_queue.dequeue()
    print(custom_queue)
    print("Peek:", custom_queue.peek())
    custom_queue.delete()
    print(custom_queue)
