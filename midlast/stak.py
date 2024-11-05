class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []
    
    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)
    
    def pop(self):
        # Remove and return the top item from the stack
        # Check if the stack is not empty to avoid IndexError
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def peek(self):
        # Return the top item of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
    
    def size(self):
        # Return the size of the stack
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())  # Output: 30
print("Stack size:", stack.size())  # Output: 2
print("Is stack empty?", stack.is_empty())  # Output: False