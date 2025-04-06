import math

# Read the number of inputs
n = int(input())

# Initialize an empty list to store numbers
numbers = []

# Read and store numbers
for i in range(n):
    try:
        num = int(input())
        numbers.append(num)
    except ValueError:

        break

# Calculate the sum of the numbers
total_sum = sum(numbers)

# Check if the sum is a perfect square
m = math.sqrt(total_sum)
if m == int(m):  # A more Pythonic way to check for integer
    print("YES")
else:
    print("NO")

