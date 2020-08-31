import time
from reverse import Node, LinkedList
start_time = time.time()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def amount(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = set()  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.add(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{duplicates}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
