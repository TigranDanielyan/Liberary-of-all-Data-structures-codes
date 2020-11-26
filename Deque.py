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

D=Deque()
print("epmtiness status: ",d.isEmpty())
D.addRear(55)
D.addRear('link')
D.addFront('lamb')
D.addFront(False)
print("size statues ",d.size())
print("epmtiness status: ",d.isEmpty())
D.addRear(6.3)
print("rear status iteam: ", d.removeRear())
print("front status iteam: ", d.removeFront())
