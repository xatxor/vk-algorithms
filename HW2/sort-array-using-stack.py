def sortArrayUsingStack(nums):
    stack = []

    while nums:
        current = nums.pop()
        while stack and stack[-1] > current:
            nums.append(stack.pop())
        stack.append(current)

    return stack
