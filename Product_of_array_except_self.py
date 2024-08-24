n: list[int] = [1, 2, 3, 4]

# Initialize prefix and postfix arrays with 1s
pre_mul: list[int] = [1] * len(n)
post_mul: list[int] = [1] * len(n)
res: list[int] = [1] * len(n)

# Calculate the prefix products
for i in range(1, len(n)):
    pre_mul[i] = pre_mul[i - 1] * n[i - 1]

# Calculate the postfix products
for i in range(len(n) - 2, -1, -1):  # Start from second last element and go backwards
    post_mul[i] = post_mul[i + 1] * n[i + 1]

# Combine the prefix and postfix products to get the result
for i in range(len(n)):
    res[i] = pre_mul[i] * post_mul[i]

print("Prefix Multiplication:", pre_mul)
print("Postfix Multiplication:", post_mul)
print("Result:", res)
