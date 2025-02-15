def solve(s, bomb):
    stack = []

    for char in s:
        stack.append(char)
        if len(stack) >= len(bomb) and "".join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    if stack:
        return "".join(stack)
    else:
        return "FRULA"
