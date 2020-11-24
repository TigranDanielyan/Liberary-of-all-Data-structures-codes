class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self):
        self.size = 266
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        multiplayer = 1
        hash_value = 0
        for character in key:
            hash_value += multiplayer * ord(character)
            multiplayer += 1
        return hash_value % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                break
            hash_value = (hash_value + 1) % self.size
        if self.slots[hash_value] is None:
            self.count += 1
        self.slots[hash_value] = item

    def get(self, key):
        hash_value = self._hash(key)
        while self.slots[hash_value] is not None:
            if self.slots[hash_value].key is key:
                return self.slots[hash_value].value
            hash_value = (hash_value + 1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


ht = HashTable()
ht.put('key1','value1')
ht.put('key2','value2')
ht.put('key3','value3')
ht.put('key5','value10')
ht.put('key6', 'value20')

print("printing original numbers")
print(ht['key1'])
print (ht['key2'])
print (ht['key3'])
print(ht['key5'])
print (ht['key6'])

print("changing before 2nd print original numbers")
ht.put('key5','value1')
ht.put('key1','value10')
print(ht['key1'])
print (ht['key2'])
print (ht['key3'])
print(ht['key5'])
print (ht['key6'])
