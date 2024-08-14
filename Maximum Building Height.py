def max_histogram_area(heights):
    stack = []
    stack.append(-1)
    max_area = 0
    index = 0

    while index < len(heights):
        # If stack is empty or the current height is greater than the top of the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top
            top_of_stack = stack.pop()
            # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar 'h'
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            # Update max_area, if needed
            max_area = max(max_area, area)

    # Now, pop the remaining bars from stack and calculate the area
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

# Example usage
l = [4, 3, 1, 5, 0, 5]
print(max_histogram_area(l))  # Output: 6
