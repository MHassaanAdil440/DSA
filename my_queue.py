class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.isempty():
            return self.items.pop(0)
        else:
            return None
        
    def isempty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def show_queue(self):
        for i in self.items:
            print(i)
    
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

# my_queue.show_queue()

my_queue.dequeue()

my_queue.show_queue()
