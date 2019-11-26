import json
Initial_Capacity = 10

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = Initial_Capacity
        self.size= 0
        self.buckets = [None]*self.capacity

    def loadData(self):
        with open("main.json") as data_file:
            self.data = json.load(data_file)
        return self.data

    def hash(self,key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx+len(key))**ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self,key,value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index]=Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node= node.next
        prev.next = Node(key,value)

    def find(self,key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

def main():
    users = HashTable()
    all_users = users.loadData()
    for key in all_users["ID"]:
        username = key
        fname = all_users["ID"][key]["name"]
        users.insert(username,fname)
        print(users.find(username))
main()
