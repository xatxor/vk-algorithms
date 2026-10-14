from collections import deque


def isPalindrome(s):
    queue = deque(s)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False

    return True
