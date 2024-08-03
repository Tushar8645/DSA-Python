# How to use collectionos.deque as a FIFO queue.

from collections import deque

custom_queue = deque(maxlen=3)
print(custom_queue)

custom_queue.append(10)
custom_queue.append(20)
custom_queue.append(30)
custom_queue.append(40)
print(custom_queue)

print(custom_queue.popleft())
print(custom_queue)

custom_queue.clear()
print(custom_queue)