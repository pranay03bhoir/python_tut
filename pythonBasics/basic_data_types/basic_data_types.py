# The following line prints the value 0.1 with 25 digits after the decimal point.
# This demonstrates how floating-point numbers are represented internally in Python,
# which may not always match exactly their expected decimal value due to binary limitations.
print(format(0.1, ".25f"))  # e.g., 0.1000000000000000055511151

# Similarly, printing 0.125 with high precision shows how some decimal fractions are exactly
# representable in binary floating-point (0.125 = 1/8), so we expect zeros after the 5.
print(format(0.125, ".25f"))  # e.g., 0.1250000000000000000000000

# This checks if the sum of three integers (1+1+1) is equal to 3.
# This should always be True because integer addition is exact.
print(1 + 1 + 1 == 3)  # Output: True

# Now, adding 0.125 three times. Since 0.125 has an exact binary representation,
# the sum should precisely equal 0.375, yielding True as output.
print(0.125 + 0.125 + 0.125 == 0.375)  # Output: True

# Adding 0.1 three times, and checking if the result is exactly equal to 0.3.
# Due to floating-point inaccuracies, this often yields False, showing that
# some decimal values cannot be represented exactly with binary floats.
print(0.1 + 0.1 + 0.1 == 0.3)  # Output: False

# Print the result of 0.1 + 0.1 + 0.1 with 25 decimal places to reveal the tiny error.
print(format(0.1 + 0.1 + 0.1, ".25f"))  # e.g., 0.3000000000000000444089209

# To reliably check for approximate equality with floats, we use a workaround:
# We check if the absolute difference between the two numbers is less than a very small threshold (e.g., 0.001).
print((abs(0.1 + 0.1 + 0.1) - 0.3) < 0.001)  # Output: True
