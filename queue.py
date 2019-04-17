class Queue:
    """This class creates a stack data structure.It's main rule is FIFO(first in and first out)"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items:
            return False #The stack is not empty.
        else:
            return True #The stack is empty.

    def enqueue(self, item):
        return self.items.append(item) #Insert a item in the end.

    def dequeue(self):
        if self.is_empty():
            print("Sorry!The queue is empty")
        else:
            return self.items.pop(0) #Removes the first item.

    def size(self):
        return len(self.items)


my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue("Shafayet Sadi")
print(my_queue.is_empty())
