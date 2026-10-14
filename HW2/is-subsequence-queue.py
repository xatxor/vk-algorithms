from collections import deque


def isSubsequence(a, b):
    queue = deque(a)

    for char in b:
        if queue and queue[0] == char:
            queue.popleft()

    return not queue
