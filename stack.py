class Stack:
	"""This class creates a stack data structure.It's main rule is FILO(first in and last out)"""
	def __init__(self):
		self.stack = []

	def is_empty(self):
		if self.stack:
			return False #The stack is not empty.
		else:
			return True #The stack is empty.

	def push(self, item):
		return self.stack.append(item) #Insert a item in the end.

	def pop(self):
		if self.is_empty():
			return 'Sorry!The stack is empty.'
		else:
			return self.stack.pop() #Removes the last item.

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[len(self.stack)-1] #See the last item.

if __name__ == '__main__':
	my_stack = Stack()
	print("The stack is empty:", my_stack.is_empty())
	print('Adding Shafayet Sadi')
	my_stack.push("Shafayet Sadi")
	print("The stack is empty:", my_stack.is_empty())