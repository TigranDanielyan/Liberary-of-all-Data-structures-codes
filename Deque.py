class CyclicDeque:

    def __init__(self):
        self.items = [None]
        self.size = 0

    def double_size(self):
        new_size = len(self.items) * 2
        new_items = []
        for i in range(new_size):
            new_items.append(None)
        for item in range(len(self.items)):
            new_items[item] = self.items[item]
        self.items = new_items

    def is_full(self):
        if self.size == len(self.items):
            return True
        return False

    def is_empty(self):
        return self.size == 0

    def insert_first(self, data):
        if self.is_full():
            self.double_size()
        if self.items[0] is None:
            self.items[0] = data
            self.size += 1
        else:
            if self.items[-1] is None:
                self.items.pop(-1)
                self.items.insert(0, data)
                self.size += 1

    def insert_last(self, data):
        if self.is_full():
            self.double_size()
        self.items[self.size] = data
        self.size += 1

    def deleteFirst(self):
        self.items.pop(0)
        self.items.append(None)
        self.size -= 1

    def deleteLast(self):
        self.items[self.size - 1] = None
        self.size -= 1

    def getFirst(self):
        return self.items[0]

    def getLast(self):
        return self.items[self.size - 1]

    def __repr__(self):
        print("Printing Cyclic Deque: ", end="\t")
        print(self.items)
        return ""

class Deque:

    def __init__(self):
        self.items = DoubleLinkedList()
        self.capacity = 8

    def add_first(self, data):
        if self.is_full():
            print("Overload!")
            return
        self.items.insert_first(data)

    def add_last(self, data):
        if self.is_full():
            print("Overload!")
            return
        self.items.insert_last(data)

    def remove_first(self):
        self.items.remove_first()

    def remove_last(self):
        self.items.remove_last()

    def get_first(self):
        return self.items.get_first()

    def get_last(self):
        return self.items.get_last()

    def is_full(self):
        return self.items.get_size() == 8

    def get_size(self):
        return self.items.get_size()

    def __repr__(self):
        current_node = self.items.get_first()
        deque = []
        while current_node is not None:
            deque.append(current_node.data)
            current_node = current_node.next
        return "Printing Deque: " + str(deque) + "\n\n"

