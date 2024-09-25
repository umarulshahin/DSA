
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