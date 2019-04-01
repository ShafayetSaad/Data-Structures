class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		if self.items:
			return False
		else:
			return True

	def enqueue(self, item):
		return self.items.append(item)

	def dequeue(self):
		if is_empty():
			print("Sorry!The queue is empty")
		else:
			return self.items.pop(0)

	def size(self):
		return len(self.items)


my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue("Shafayet Sadi")
print(my_queue.is_empty())