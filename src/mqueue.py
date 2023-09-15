from customer import Customer


class MQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, element: Customer):
        self._queue.insert(0, element)

    def enqueue_priority(self, element: Customer):
        self._queue.append(element)

    def dequeue(self) -> Customer:
        return self._queue.pop()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return len(self._queue) == 0


# Testing queue functionality
if __name__ == "__main__":
    q = MQueue()
    q.enqueue("1")
    q.enqueue("2")
    q.enqueue("3")
    q.enqueue_priority("4")
    print("LENGTH ", len(q))
    while not q.is_empty():
        print(q.dequeue())
