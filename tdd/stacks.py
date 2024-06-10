class MyStack:

    def __init__(self):
        self.stack = []

    def add_to_stack(self, item):
        return self.stack.append(item)

    def pop(self):
        del self.stack[-1]
        return self.stack