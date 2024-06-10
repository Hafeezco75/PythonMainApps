class MyQueue:

    def __init__(self):
        self.queue = []

    def add_to_queue(self, item):
        return self.queue.append(item)

    def remove_from_queue(self):
        del self.queue[2]
        return self.queue
