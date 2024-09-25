
 #* stack using importcollection deque 

import collections

stack= collections.deque()
print(not stack)
stack.append(10)
stack.append(30)
stack.append(50)
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# stack using import collection LifeQueue

import queue
stack=queue.LifoQueue(3)
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40,timeout=1)


print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get(timeout=1))