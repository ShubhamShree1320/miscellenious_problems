def longest_valid_subsequence(s):
    stack = []
    max_length = 0
    last_invalid_index = -1
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    max_length = max(max_length, i - last_invalid_index)
            else:
                last_invalid_index = i
    
    return max_length

s = "((((((((((((((((()(()))))))))))))"
print(longest_valid_subsequence(s))
