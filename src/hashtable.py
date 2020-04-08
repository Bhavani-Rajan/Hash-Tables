# '''
# Linked List hash table key/value pair
# '''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"<{self.key}, {self.value}>"
    
class LinkedList:
    def __init__(self):
        self.head = None
    def remove(self, key):
        '''
        Find and remove the node with the given value
        '''
        if not self.head:
            print("Error: Value not found")
        elif self.head.key == key:
            # Remove head value
            self.head = self.head.next
        else:
            parent = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    # Remove value
                    parent.next = current.next
                    return
                current = current.next
            print("Error: Value not found")


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        
        # # Hashmod the key to find the bucket
        # index = self._hash_mod(key)
        # # Check if a pair already exists in the bucket
        # pair = self.storage[index]
        # if pair is not None:
        #     # If so, overwrite the key/value and throw a warning
        #     if pair.key != key:
        #         print("Warning: Overwriting value")
        #         pair.key = key
        #     pair.value = value
        # else:
        #     # If not, Create a new LinkedPair and place it in the bucket
        #     self.storage[index] = LinkedPair(key, value)

        # Hashmod the key to find the bucket
        index = self._hash_mod(key)
        node = self.storage[index]
        
        if node is not None: #hash collision 
            #print("hash collision detected")
            while node is not None: # iterates through all non-Null keys of the nodes within the hash table location
                if node.key == key: #if the current node's key matches the new insertion key
                    node.value = value #update the value
                    break
                elif node.next == None: #if the current node's next is None we are at the tail
                    node.next = Node(key,value) #create new Node at tail location
                    break
                node = node.next  
        else:
            self.storage[index] = Node(key,value)





    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)

        # # Check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     # If so, remove that pair
        #     self.storage[index] = None
        # else:
        #     # Else print warning
        #     print("Warning: Key does not exist")

        index = self._hash_mod(key) 
        ll = LinkedList()
        ll.head = self.storage[index]
        ll.remove(key)
        self.storage[index] = ll.head

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get the index from hashmod
        # index = self._hash_mod(key)

        # # Check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     # If so, return the value
        #     return self.storage[index].value
        # else:
        #     # Else return None
        #     return None

        index = self._hash_mod(key)
        node = self.storage[index] 
        while node:
            if node.key == key:
                return node.value
            node = node.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pairs = []
        for bucket in self.storage:
            if bucket != None:
                node = bucket
                while(node):
                    pairs.append((node.key,node.value))
                    if(node.next == None):
                        break
                    node = node.next
        self.capacity *= 2  # Number of buckets in the hash table
        self.storage = [None] * self.capacity
        for key,value in pairs:
            self.insert(key,value)
        return
