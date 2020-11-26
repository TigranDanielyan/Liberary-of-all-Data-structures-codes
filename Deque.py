class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d=Deque()
print("epmtiness status: ",d.isEmpty())
d.addRear(55)
d.addRear('link')
d.addFront('lamb')
d.addFront(False)
print("size statues ",d.size())
print("epmtiness status: ",d.isEmpty())
d.addRear(8.4)
print("rear status iteam: ", d.removeRear())
print("front status iteam: ", d.removeFront())
