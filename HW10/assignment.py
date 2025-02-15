class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        enqueue를 구현해 주세요.
        """
        raise NotImplementedError("enqueue 메서드를 구현해 주세요.")

    def dequeue(self):
        """
        dequeue를 구현해 주세요.
        """
        raise NotImplementedError("dequeue 메서드를 구현해 주세요.")

    def size(self):
        return len(self.items)
    
    def __str__(self):
        """
        queue에 있는 내용을 출력해주세요.
        """
        raise NotImplementedError("queue를 출력해 주세요.")
