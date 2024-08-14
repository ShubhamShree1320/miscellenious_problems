def valid_parenthesis(s):
    stack = []

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if not stack:
                return False
            else:
                top = stack.pop()
                if not ((char == ')' and top == '(') or (char == ']' and top == '[') or (char == '}' and top == '{')):
                    return False

    return not stack


print(valid_parenthesis(input()))