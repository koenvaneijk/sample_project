import random

def generate_random_number(lower_bound=1, upper_bound=100):
  """Generates a random integer within the specified bounds (inclusive)."""
  if not isinstance(lower_bound, int) or not isinstance(upper_bound, int):
      raise TypeError("Bounds must be integers.")
  if lower_bound > upper_bound:
      raise ValueError("Lower bound cannot be greater than upper bound.")
  return random.randint(lower_bound, upper_bound)

if __name__ == "__main__":
  # Generate a random integer between 1 and 100 (inclusive)
  random_number = generate_random_number(1, 100)
  # Print the generated number
  print(f"Generated random number: {random_number}")