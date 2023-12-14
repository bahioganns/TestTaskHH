"""Task 2: FIFO buffer."""

from collections import deque

class BufferList:
    """Use list to represent the FIFO buffer."""
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.start = 0
        self.end = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if not self.is_full():
            self.buffer[self.end] = item
            self.end = (self.end + 1) % self.capacity
            self.size += 1
        else:
            raise Exception("Buffer is full")

    def dequeue(self):
        if not self.is_empty():
            item = self.buffer[self.start]
            self.start = (self.start + 1) % self.capacity
            self.size -= 1
            return item
        else:
            raise Exception("Buffer is empty")

class BufferDeque:
    """Use deque to represent the FIFO buffer."""
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def is_full(self):
        return len(self.buffer) == self.buffer.maxlen

    def enqueue(self, item):
        if self.is_full():
            self.buffer.popleft()
        self.buffer.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.popleft()
        else:
            raise Exception("Buffer is empty")


# BufferDeque Showcase
buffer_deque = BufferDeque(3)

assert buffer_deque.is_empty(), "Buffer should be empty"

buffer_deque.enqueue(1)
buffer_deque.enqueue(2)

assert not buffer_deque.is_full(), "Buffer should not be full"

buffer_deque.enqueue(3)

assert buffer_deque.is_full(), "Buffer should be full"
assert buffer_deque.dequeue() == 1, "The dequeued element should be 1"
assert not buffer_deque.is_empty(), "Buffer should not be empty"


# BufferList showcase
buffer_list = BufferList(3)

assert buffer_list.is_empty(), "Buffer should be empty"

buffer_list.enqueue(1)
buffer_list.enqueue(2)

assert not buffer_list.is_full(), "Buffer should not be full"

buffer_list.enqueue(3)

assert buffer_list.is_full(), "Buffer should be full"
assert buffer_list.dequeue() == 1, "The dequeued element should be 1"
assert not buffer_list.is_empty(), "Buffer should not be empty"
