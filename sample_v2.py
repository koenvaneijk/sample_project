import random

# Generate 10 random integers between 1 and 100 (inclusive)
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Print the generated numbers
print("Generated random numbers:")
for number in random_numbers:
    print(number)