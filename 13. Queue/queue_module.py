import queue as q

custom_queue = q.Queue(maxsize=3)
print(custom_queue.queue)
print("Is empty:", custom_queue.empty())
custom_queue.put(10)
custom_queue.put(20)
custom_queue.put(30)
print(custom_queue.queue)

print("Size:", custom_queue.qsize())
print("Is full:", custom_queue.full())
print("Get first value:", custom_queue.get())
print(custom_queue.queue)
