# How to use multiprocessing.Queue as a FIFO queue.

from multiprocessing import Queue

custom_queue = Queue(maxsize=3)
custom_queue.put(10)
print(custom_queue.get())