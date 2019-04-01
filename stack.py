class Stack:
	def __init__(self):
		self.stack = []

	def is_empty(self):
		if self.stack:
			return False
		else:
			return True

	def push(self, item):
		return self.stack.append(item)

	def pop(self):
		if is_empty():
			return 'Sorry!The stack is empty.'
		else:
			return self.stack.pop()

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1]


my_stack = Stack()
print(my_stack.is_empty())
my_stack.push("Shafayet Sadi")
print(my_stack.is_empty())
