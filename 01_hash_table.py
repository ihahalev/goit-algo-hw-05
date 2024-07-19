class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        print(key_hash, key_value)

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        if not len(self.table):
            print(key,"len None")
            return None
        key_hash = self.hash_function(key)
        if self.table[key_hash] is None or not len(self.table[key_hash]):
            print(key, key_hash,"None")
            return None
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    value = pair[1]
                    if len(self.table[key_hash]) > 1:
                        self.table[key_hash].remove(pair)
                        print(key, self.table)
                    else:
                        self.table[key_hash] = None
                        print(key, self.table)
                    return value

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
print(H.table)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("passion fruit", 40)
H.insert("peach", 50)
H.insert("cherry", 60)

print(H.table)
# print(H.get("apple"))   # Виведе: 10
# print(H.get("orange"))  # Виведе: 20
# print(H.get("banana"))  # Виведе: 30
# print(H.get("passion fruit"))   # Виведе: 40
# print(H.get("peach"))  # Виведе: 50
# print(H.get("cherry"))  # Виведе: 60

print(H.delete("apple"))
print(H.delete("orange"))
print(H.delete("banana"))
print(H.delete("passion fruit"))
print(H.delete("peach"))
print(H.delete("cherry"))

H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("passion fruit", 40)
H.insert("peach", 50)
H.insert("cherry", 60)