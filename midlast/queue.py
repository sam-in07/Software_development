class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []
    
    def enqueue(self, item):
        # Add an item to the end of the queue
        self.queue.append(item)
    
    def dequeue(self):
        # Remove and return the front item of the queue
        # Check if the queue is not empty to avoid IndexError
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    def front(self):
        # Return the front item of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"
    
    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0
    
    def size(self):
        # Return the size of the queue
        return len(self.queue)

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.front())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 10
print("Queue size:", queue.size())  # Output: 2
print("Is queue empty?", queue.is_empty())  # Output: False