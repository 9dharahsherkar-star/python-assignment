class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print(self.items.pop(), "popped from stack")

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", self.items[-1])



s = Stack()
print("Stack created")
s.push(10)
s.peek()
s.push(20)
s.peek()
s.push(30)
s.pop()
