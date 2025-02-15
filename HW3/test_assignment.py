import pytest
import numpy as np
import assignment

def test_enqueue():
    queue = assignment.Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    assert queue.peek() == 1

def test_dequeue():
    queue = assignment.Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.peek() == 2
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()

def test_dequeue_empty():
    queue = assignment.Queue()
    assert queue.dequeue() == "Queue is empty"
