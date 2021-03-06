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

Q=Queue()
Q.enqueue(4)
Q.enqueue('dog')
Q.enqueue(True)
print("printing size:", Q.size())
Q.dequeue()
print("printing size:", Q.size())
Q.dequeue()
print("printing size:", Q.size())
print("checking if queue is empty:", Q.isEmpty())
Q.dequeue()
print("printing size:", Q.size())
print("checking if queue is empty:", Q.isEmpty())
