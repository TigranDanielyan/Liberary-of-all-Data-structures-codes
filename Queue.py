class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print("printing size:", q.size())
q.dequeue()
print("printing size:", q.size())
q.dequeue()
print("printing size:", q.size())
print("checking if queue is empty:", q.isEmpty())
q.dequeue()
print("printing size:", q.size())
print("checking if queue is empty:", q.isEmpty())
