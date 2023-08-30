from collections import deque

queue = deque([1,2,6,5,8,9])
print(queue)
queue.append(33)
print(queue)
queue.append(44)
queue.append(55)
queue.append(66)
print(queue)

queue.pop()
print(queue)

queue.appendleft(10)
print(queue)

queue.popleft()
print(queue)