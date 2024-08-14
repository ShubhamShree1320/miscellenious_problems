import heapq
import numpy as np
# Original matrix
matrix = [[1,2],[1,3]]

lst=[]
for i in matrix:
    lst=lst+i
print(lst)
# # # Reshape the flat list back into a 2D matrix with the same dimensions
# # rows, cols = len(matrix), len(matrix[0])
# # reshaped_matrix = [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]

# # Function to pop a specific index element
# def heappop_specific(heap, index):
#     index=index-1
#     # Replace the target element with float('-inf') (or any very small value)
#     heap[index] = float('-inf')
#     print(f"Updated heap: {heap}")
#     # Move the new root element to the correct position
#     heapq._siftup(heap, index)
    
#     # Pop the root element
#     return heapq.heappop(heap)

# # # Example: Pop the element at index 5
# # popped_element = heappop_specific(flat_list, 8)
# # # print(f"Popped element: {popped_element}")
# # # print(f"Updated heap: {flat_list}")
# print(flat_list[8-1])