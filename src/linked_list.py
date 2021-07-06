class Node:
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, key,value):
        self.head = Node(key,value, self.head)

    def remove(self, key):
        '''
        Find and remove the node with the given value
        '''
        if not self.head:
            print("Warning: Key not found")
        elif self.head.key == key:
            # Remove head value
            self.head = self.head.next
        else:
            previous = self.head
            current = self.head.next
            while current:
                if current.key == key:
                    # Remove value
                    previous.next = current.next
                    return
                current = current.next
            print("Warning: Key not found")

    def update(self, key,value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
    
    def contains(self, key):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def retrieve(self,key):
        current= self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def print(self):
        current = self.head
        ll_str = ""
        while current:
            ll_str += f"{current.key} - {current.value}"
            current = current.next
            ll_str += " -> "
        ll_str += "None"
        print(ll_str)

# from linked_list import *
# ll = LinkedList()
# ll.print()
# ll.add_to_head(1,'a')
# ll.add_to_head(2,'b')
# ll.add_to_head(3,'c')
# ll.print()
# ll.remove(2)
# ll.print()
# ll.update(1,'s')
# ll.print()