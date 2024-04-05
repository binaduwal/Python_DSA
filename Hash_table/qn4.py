# Implement hash table where collisions are handled using linear probing. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return None
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return None
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hash map full")
                
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)

t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["jun 22"] = 1
t["oct 28"] = 234
t["feb 19"] = 99
t["dec 1"] = 34
t["sept 17"] = 41
t["july 1"] = 54
t["sept 24"] = 97
t["jan 4"] = 0
del t["march 6"]